"""Unit tests for the project version fallback logic."""

from unittest.mock import patch

from {{ cookiecutter.package_name }}.api.main import get_project_version


def test_main_version_fallback() -> None:
    """Tests the fallback version logic in main.py when VERSION file is missing or unreadable."""
    import importlib.metadata
    with patch("importlib.metadata.version") as mock_version:
        # Simulate that the package is not installed
        mock_version.side_effect = importlib.metadata.PackageNotFoundError

        with patch("pathlib.Path.read_text") as mock_read:
            # Simulate the absence of the VERSION file
            mock_read.side_effect = Exception("File not found")

            # Call the version retrieval function
            version = get_project_version()

            # Verify that the fallback activates correctly
            assert version == "0.1.0"
