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