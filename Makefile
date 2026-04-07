.PHONY: digest validate

digest:
	uv run --with gitingest gitingest .
	explorer.exe .

validate:
	@echo "🔍 Validating template generation..."
	@mkdir -p tmp_test
	@uvx cookiecutter data-science --no-input -o ./tmp_test --overwrite-if-exists
	@echo "✅ Template generated successfully in ./tmp_test/project_name"
	@echo "🧹 Cleaning up..."
	@rm -rf tmp_test
	@echo "✨ Validation complete."

bump: ## Bump the project version (using commitizen)
	uv run --with commitizen cz bump

release: ## Push the latest commits and tags to origin main
	git push origin main --follow-tags
	git push --tags

clean: ## Remove temporary files and caches
	rm -rf .venv
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml dist/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Cleaned environment caches and .venv"