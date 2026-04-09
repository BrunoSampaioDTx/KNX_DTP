#!/usr/bin/env python3
"""
Standalone PDF-to-Markdown conversion script using Docling.

Aligns with the project's existing Docling pipeline (see docling_processor.py)
while being fully self-contained — no imports from app/ or config/.

Usage:
    # Single file
    python aux/convert_pdf_to_markdown.py report.pdf

    # Custom output
    python aux/convert_pdf_to_markdown.py report.pdf -o output/report.md

    # Batch convert a directory
    python aux/convert_pdf_to_markdown.py ./documents/ -o ./markdown_output/

    # With OCR for scanned PDFs
    python aux/convert_pdf_to_markdown.py scanned.pdf --ocr

    # Accurate table extraction + verbose
    python aux/convert_pdf_to_markdown.py report.pdf --accurate-tables --verbose
"""

import argparse
import gc
import logging
import os
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("pdf2md")


def setup_logging(verbose: bool = False, quiet: bool = False) -> None:
    """Configure logging based on verbosity flags."""
    if quiet:
        level = logging.ERROR
    elif verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )


def build_converter(
    ocr: bool = False,
    accurate_tables: bool = False,
    images_scale: float = 1.5,
):
    """
    Build a Docling DocumentConverter with the same pipeline config
    used in docling_processor.py (lines 46-59).
    """
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
    from docling.document_converter import DocumentConverter, PdfFormatOption

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = ocr
    pipeline_options.allow_external_plugins = False
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.mode = (
        TableFormerMode.ACCURATE if accurate_tables else TableFormerMode.FAST
    )
    pipeline_options.images_scale = images_scale
    pipeline_options.generate_picture_images = False
    pipeline_options.generate_page_images = False

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    logger.debug(
        "Converter built — OCR=%s, accurate_tables=%s, images_scale=%s",
        ocr, accurate_tables, images_scale,
    )
    return converter


def split_pdf_into_chunks(pdf_path: Path, batch_size: int, tmp_dir: Path) -> list[tuple[Path, int]]:
    """
    Split a PDF into chunks of batch_size pages using pypdf.
    Returns list of (chunk_path, first_page_number_1based).
    """
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    chunks: list[tuple[Path, int]] = []

    for start in range(0, total_pages, batch_size):
        end = min(start + batch_size, total_pages)
        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        chunk_path = tmp_dir / f"chunk_{start + 1:04d}_{end:04d}.pdf"
        with open(chunk_path, "wb") as f:
            writer.write(f)
        chunks.append((chunk_path, start + 1))
        logger.debug("Created chunk: pages %d–%d → %s", start + 1, end, chunk_path.name)

    logger.info("Split %d pages into %d chunks of ≤%d pages", total_pages, len(chunks), batch_size)
    return chunks


def convert_pdf_to_markdown(
    converter,
    pdf_path: Path,
    output_path: Path,
    page_markers: bool = True,
    batch_size: int | None = None,
) -> bool:
    """
    Convert a single PDF to Markdown using Docling.

    If batch_size is set, the PDF is split into chunks of that many pages
    and each chunk is converted separately to avoid OOM on large documents.
    Memory is released between chunks via gc.collect().

    Returns True on success, False on failure.
    """
    from docling_core.types.doc import ImageRefMode

    if batch_size is not None:
        return _convert_batched(converter, pdf_path, output_path, page_markers, batch_size)

    try:
        logger.info("📄 Converting: %s", pdf_path.name)
        start = time.time()

        result = converter.convert(str(pdf_path))
        doc = result.document

        # --- Page-aware markdown generation ---
        if page_markers and hasattr(doc, "pages") and doc.pages:
            parts: list[str] = []
            for idx, page_no in enumerate(sorted(doc.pages.keys()), start=1):
                page_md = doc.export_to_markdown(
                    page_no=page_no,
                    image_mode=ImageRefMode.PLACEHOLDER,
                )
                if page_md.strip():
                    parts.append(f"<!-- PAGE {idx} -->\n{page_md.strip()}")
            markdown_text = "\n\n".join(parts)
        else:
            markdown_text = doc.export_to_markdown(
                image_mode=ImageRefMode.PLACEHOLDER
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown_text, encoding="utf-8")

        elapsed = time.time() - start
        logger.info(
            "✅ %s → %s (%.1fs)", pdf_path.name, output_path, elapsed
        )
        return True

    except Exception as e:
        logger.error("❌ Failed to convert %s: %s", pdf_path.name, e)
        logger.debug("Traceback:", exc_info=True)
        return False


def _convert_batched(
    converter,
    pdf_path: Path,
    output_path: Path,
    page_markers: bool,
    batch_size: int,
) -> bool:
    """Convert a large PDF in page-batched chunks to limit memory usage."""
    from docling_core.types.doc import ImageRefMode

    logger.info("📄 Converting in batches of %d pages: %s", batch_size, pdf_path.name)
    start = time.time()
    all_parts: list[str] = []
    global_page_idx = 0
    had_errors = False

    with tempfile.TemporaryDirectory(prefix="pdf2md_") as tmp_dir:
        try:
            chunks = split_pdf_into_chunks(pdf_path, batch_size, Path(tmp_dir))
        except Exception as e:
            logger.error("❌ Failed to split PDF: %s", e)
            logger.debug("Traceback:", exc_info=True)
            return False

        for chunk_path, first_page in chunks:
            try:
                logger.info(
                    "  🔄 Processing chunk starting at page %d ...", first_page
                )
                result = converter.convert(str(chunk_path))
                doc = result.document

                if page_markers and hasattr(doc, "pages") and doc.pages:
                    for page_no in sorted(doc.pages.keys()):
                        global_page_idx += 1
                        page_md = doc.export_to_markdown(
                            page_no=page_no,
                            image_mode=ImageRefMode.PLACEHOLDER,
                        )
                        if page_md.strip():
                            all_parts.append(
                                f"<!-- PAGE {global_page_idx} -->\n{page_md.strip()}"
                            )
                else:
                    chunk_md = doc.export_to_markdown(
                        image_mode=ImageRefMode.PLACEHOLDER
                    )
                    if chunk_md.strip():
                        all_parts.append(chunk_md.strip())
                    if page_markers:
                        global_page_idx += batch_size

            except Exception as e:
                had_errors = True
                logger.error(
                    "⚠️  Chunk starting at page %d failed: %s", first_page, e
                )
                logger.debug("Traceback:", exc_info=True)
            finally:
                # Free memory between chunks
                gc.collect()

    if not all_parts:
        logger.error("❌ No content extracted from %s", pdf_path.name)
        return False

    markdown_text = "\n\n".join(all_parts)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_text, encoding="utf-8")

    elapsed = time.time() - start
    status = "⚠️" if had_errors else "✅"
    logger.info(
        "%s %s → %s (%.1fs, %d chunks%s)",
        status, pdf_path.name, output_path, elapsed, len(chunks) if 'chunks' in dir() else 0,
        ", some chunks failed" if had_errors else "",
    )
    return True


def _timestamped_name(pdf_path: Path) -> str:
    """Generate filename: {stem}_{DD_MM_YYYY_HH_MM}.md"""
    stamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
    return f"{pdf_path.stem}_{stamp}.md"


def resolve_output_path(
    pdf_path: Path, output_arg: str | None, batch_mode: bool
) -> Path:
    """
    Determine the output .md file path.

    Rules:
      - No -o flag          → output/{stem}_{timestamp}.md
      - -o is a directory   → place timestamped .md inside that directory
      - -o is a file path   → use it directly (single-file mode only)
    """
    name = _timestamped_name(pdf_path)

    if output_arg is None:
        out_dir = Path(__file__).parent / "output"
        out_dir.mkdir(parents=True, exist_ok=True)
        return out_dir / name

    out = Path(output_arg)

    if batch_mode or out.is_dir() or output_arg.endswith(os.sep):
        out.mkdir(parents=True, exist_ok=True)
        return out / name

    return out


def collect_pdfs(source: Path) -> list[Path]:
    """Collect PDF files from a path (single file or directory)."""
    if source.is_file():
        if source.suffix.lower() != ".pdf":
            logger.error("❌ File is not a PDF: %s", source)
            return []
        return [source]

    if source.is_dir():
        pdfs = sorted(source.glob("**/*.pdf"))  # recursive
        if not pdfs:
            logger.warning("⚠️  No PDF files found in %s", source)
        return pdfs

    logger.error("❌ Path does not exist: %s", source)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown using Docling",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  %(prog)s report.pdf                          # single file → report.md
  %(prog)s report.pdf -o out/report.md         # custom output path
  %(prog)s ./pdfs/ -o ./markdown/              # batch convert directory
  %(prog)s scanned.pdf --ocr                   # enable OCR
  %(prog)s report.pdf --accurate-tables -v     # better tables + verbose
""",
    )
    parser.add_argument(
        "source",
        help="Path to a PDF file or a directory containing PDFs",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output file (.md) or directory. Default: same location as source with .md extension",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Enable OCR for scanned/image-based PDFs",
    )
    parser.add_argument(
        "--accurate-tables",
        action="store_true",
        help="Use accurate (slower) table structure recognition",
    )
    parser.add_argument(
        "--no-page-markers",
        action="store_true",
        help="Disable <!-- PAGE N --> comment markers between pages",
    )
    parser.add_argument(
        "--images-scale",
        type=float,
        default=1.5,
        help="Resolution scale for internal page images (default: 1.5). "
             "Lower values use less memory. Original was 3.0.",
    )
    parser.add_argument(
        "--batch-pages",
        type=int,
        default=None,
        metavar="N",
        help="Process the PDF in chunks of N pages to limit memory usage. "
             "Requires 'pypdf' package. Recommended: 20–50 for large documents.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed debug output",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Only show errors",
    )
    args = parser.parse_args()

    # --- Setup ---
    setup_logging(verbose=args.verbose, quiet=args.quiet)

    source = Path(args.source)
    pdfs = collect_pdfs(source)
    if not pdfs:
        return 1

    batch_mode = len(pdfs) > 1

    logger.info("🔧 Loading Docling (this may take a moment on first run)...")
    logger.info("   OCR=%s, accurate_tables=%s, images_scale=%s",
                args.ocr, args.accurate_tables, args.images_scale)
    if args.batch_pages:
        logger.info("   batch_pages=%d (chunked mode)", args.batch_pages)
    converter = build_converter(
        ocr=args.ocr,
        accurate_tables=args.accurate_tables,
        images_scale=args.images_scale,
    )

    # --- Convert ---
    success = 0
    failures = 0

    for pdf in pdfs:
        out_path = resolve_output_path(pdf, args.output, batch_mode)
        ok = convert_pdf_to_markdown(
            converter,
            pdf,
            out_path,
            page_markers=not args.no_page_markers,
            batch_size=args.batch_pages,
        )
        if ok:
            success += 1
        else:
            failures += 1

    # --- Summary ---
    if batch_mode or not args.quiet:
        logger.info("─" * 40)
        logger.info(
            "📊 Done — %d converted, %d failed, %d total",
            success, failures, len(pdfs),
        )

    return 1 if failures > 0 else 0


if __name__ == "__main__":
    sys.exit(main())

     # python convert_pdf_to_markdown.py "03_07_02 Datapoint Types v02.02.01 AS.pdf" --batch-pages 30 --images-scale 1.0 -o ./aux__aa/output.md -v --accurate-tables 