# KNX Datapoint Types Parser

Extracts and structures the **KNX Datapoint Types** specification (document 03.07.02) from its PDF into machine-readable JSON and SQL.

## Pipeline

```
PDF ──► Markdown ──► JSON ──► SQL / PostgreSQL
```

1. **`convert_pdf_to_markdown.py`** — Converts the KNX spec PDF to Markdown using [Docling](https://github.com/DS4SD/docling) with accurate table extraction.
2. **`parse_md_to_json.py`** — Parses the Markdown into structured JSON with full DPT metadata (ranges, units, resolution, encoding, value maps, etc.).
3. **`sql_to_json.py`** — Exports from PostgreSQL back to JSON (requires `psycopg2`).
4. **`add_data_type.py`** — Enriches the JSON with C# `DataType` enum mappings.

## Project Structure

```
├── input/                          # Source files
│   ├── 03_07_02 ... AS.pdf         # KNX spec PDF (251 pages)
│   ├── 03_07_02 ... AS.md          # Converted Markdown
│   └── knx_datapoint_types.json    # Reference / enrichment JSON
├── output/                         # Generated files
│   ├── dpt_new.json                # Parser output
│   └── ...
├── testing/                        # Validation scripts
│   ├── check_units.py              # Unit string validation
│   ├── check_f32_compare.py        # F32 field comparison vs reference
│   ├── check_omega.py              # Unicode Ω normalization check
│   └── check2.py … check4.py      # Additional checks
├── convert_pdf_to_markdown.py      # PDF → Markdown (Docling)
├── parse_md_to_json.py             # Markdown → JSON parser
├── sql_to_json.py                  # PostgreSQL → JSON export
├── add_data_type.py                # DataType enum enrichment
├── knx_datapoint_types.sql         # Database schema + seed data
├── Dockerfile.pdf2md               # Docker image for PDF conversion
├── docker-compose.yml              # All services (DB, tools)
└── Makefile                        # Task runner
```

## Prerequisites

- **Docker** & **Docker Compose** (for containerised pipeline and database)
- **Python 3.11+** (for running scripts locally)
- **make** (optional — `choco install make` on Windows, or use commands directly)

## Quick Start

### Run the full pipeline in Docker

```bash
make build      # Build the pdf2md image (first time only)
make pipeline   # PDF → Markdown → JSON
```

### Run steps individually

```bash
make convert    # PDF → Markdown only
make parse      # Markdown → JSON only
```

### Database

```bash
make db         # Start PostgreSQL (localhost:5432) + pgAdmin (localhost:8080)
make db-down    # Stop all containers
```

pgAdmin credentials: `bruno@example.com` / `admin`

### Run tests

```bash
make test          # All validation scripts
make test-units    # Unit string checks only
make test-f32      # F32 comparison check
make test-omega    # Unicode Omega check
```

### Without Make

```bash
# Build & run pipeline
docker compose build pdf2md
docker compose --profile tools up parse-json

# Start database
docker compose up -d postgres pgadmin

# Run tests
python testing/check_units.py
python testing/check_f32_compare.py
```

## Docker Services

| Service       | Image               | Profile | Ports         |
|---------------|---------------------|---------|---------------|
| `postgres`    | postgres:17-alpine  | default | 5432          |
| `pgadmin`     | dpage/pgadmin4      | default | 8080 → 80    |
| `pdf2md`      | Dockerfile.pdf2md   | tools   | —             |
| `parse-json`  | python:3.11-slim    | tools   | —             |

## Output Schema

Each entry in the generated JSON contains:

| Field                       | Description                                  |
|-----------------------------|----------------------------------------------|
| `dpt_id`                    | e.g. `"1.001"`                               |
| `dpt_main_number`           | Main type number (e.g. `1`)                  |
| `dpt_sub_number`            | Sub type number (e.g. `1`)                   |
| `dpt_name`                  | e.g. `"DPT_Switch"`                          |
| `description`               | Human-readable description                   |
| `format_code`               | e.g. `"B1"`, `"N8"`, `"F16"`                |
| `size_bits`                 | Size in bits                                 |
| `size_bytes`                | Size in bytes                                |
| `data_type_category`        | Boolean, Unsigned, Signed, Float, enum, etc. |
| `value_min` / `value_max`   | Value range                                  |
| `unit`                      | SI unit string (Unicode-normalised)          |
| `resolution`                | Numeric resolution                           |
| `encoding`                  | Encoding description                         |
| `coefficient`               | Scaling coefficient                          |
| `use_scope`                 | Functional block scope (e.g. `"G"`)          |
| `application_domain`        | HVAC, lighting, common, etc.                 |
| `value_map`                 | Discrete value → label mappings              |
| `notes`                     | Additional notes from the spec               |
| `sparkplug_data_type`       | Sparkplug B type name (e.g. `"UInt8"`)       |
| `sparkplug_data_type_value` | Sparkplug B numeric type ID (e.g. `5`)       |
| Field                       | Description                                  |
|-----------------------------|----------------------------------------------|
| `dpt_id`                    | e.g. `"1.001"`                               |
| `dpt_main_number`           | Main type number (e.g. `1`)                  |
| `dpt_sub_number`            | Sub type number (e.g. `1`)                   |
| `dpt_name`                  | e.g. `"DPT_Switch"`                          |
| `description`               | Human-readable description                   |
| `format_code`               | e.g. `"B1"`, `"N8"`, `"F16"`                |
| `size_bits`                 | Size in bits                                 |
| `size_bytes`                | Size in bytes                                |
| `data_type_category`        | Boolean, Unsigned, Signed, Float, enum, etc. |
| `value_min` / `value_max`   | Value range                                  |
| `unit`                      | SI unit string (Unicode-normalised)          |
| `resolution`                | Numeric resolution                           |
| `encoding`                  | Encoding description                         |
| `coefficient`               | Scaling coefficient                          |
| `use_scope`                 | Functional block scope (e.g. `"G"`)          |
| `application_domain`        | HVAC, lighting, common, etc.                 |
| `value_map`                 | Discrete value → label mappings              |
| `notes`                     | Additional notes from the spec               |
| `sparkplug_data_type`       | Sparkplug B type name (e.g. `"UInt8"`)       |
| `sparkplug_data_type_value` | Sparkplug B numeric type ID (e.g. `5`)            |
| `use_scope`                 | Functional block scope (e.g. `"G"`)      |
| `application_domain`        | HVAC, lighting, common, etc.             |
| `value_map`                 | Discrete value → label mappings          |
| `notes`                     | Additional notes from the spec           |
| `sparkplug_data_type`       | Sparkplug B type name (e.g. `"UInt8"`)   |
| `sparkplug_data_type_value` | Sparkplug B numeric type ID (e.g. `5`)    
| `sparkplug_data_type`  | Sparkplug B type name (e.g. `"Boolean"`, `"UInt8"`, `"Float"`) |
| `sparkplug_data_type_value` | Sparkplug B numeric type ID (e.g. `11`) |        |
| `use_scope`                 | Functional block scope (e.g. `"G"`)          |
| `application_domain`        | HVAC, lighting, common, etc.                 |
| `value_map`                 | Discrete value -> label mappings             |
| `notes`                     | Additional notes from the spec               |
| `sparkplug_data_type`       | Sparkplug B type name (e.g. `"UInt8"`)       |
| `sparkplug_data_type_value` | Sparkplug B numeric type ID (e.g. `5`)       |
