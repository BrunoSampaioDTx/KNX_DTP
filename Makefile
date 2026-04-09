.PHONY: help build convert parse pipeline db db-down clean test test-units test-f32 test-omega

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# ── Docker builds ───────────────────────────────────────────────────────────

build: ## Build the pdf2md Docker image
	docker compose build pdf2md

# ── Pipeline steps ──────────────────────────────────────────────────────────

convert: ## Run PDF → Markdown conversion in Docker
	docker compose run --rm pdf2md

parse: ## Run Markdown → JSON parser in Docker
	docker compose run --rm parse-json

pipeline: ## Run full pipeline: PDF → MD → JSON
	docker compose --profile tools up parse-json
	@echo "Pipeline complete. Check output/ for results."

# ── Database ────────────────────────────────────────────────────────────────

db: ## Start PostgreSQL + pgAdmin
	docker compose up -d postgres pgadmin
	@echo "PostgreSQL: localhost:5432  pgAdmin: http://localhost:8080"

db-down: ## Stop PostgreSQL + pgAdmin
	docker compose down

# ── Testing ─────────────────────────────────────────────────────────────────

test: ## Run all check scripts
	@echo "── check_units ──"
	python testing/check_units.py
	@echo ""
	@echo "── check_units_grouped ──"
	python testing/check_units_grouped.py
	@echo ""
	@echo "── check_f32_compare ──"
	python testing/check_f32_compare.py
	@echo ""
	@echo "── check_omega ──"
	python testing/check_omega.py
	@echo ""
	@echo "── check2 ──"
	python testing/check2.py
	@echo ""
	@echo "── check3 ──"
	python testing/check3.py
	@echo ""
	@echo "── check4 ──"
	python testing/check4.py

test-units: ## Run unit validation checks
	python testing/check_units.py
	python testing/check_units_grouped.py

test-f32: ## Run F32 comparison check
	python testing/check_f32_compare.py

test-omega: ## Run Unicode Omega check
	python testing/check_omega.py

# ── Cleanup ─────────────────────────────────────────────────────────────────

clean: ## Remove generated output files
	rm -f output/dpt_new*.json output/output.md output/output.txt
