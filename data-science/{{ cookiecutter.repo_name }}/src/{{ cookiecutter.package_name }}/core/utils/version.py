"""Project version utilities."""

import importlib.metadata

from .paths import PROJECT_ROOT


def get_project_version() -> str:
    """Get the project version from package metadata or fallback to VERSION file.

    Returns:
        str: The version string.

    """
    try:
        # Try to get the version from installed package metadata
        return importlib.metadata.version("{{ cookiecutter.package_name }}")
    except importlib.metadata.PackageNotFoundError:
        # Fallback to reading the VERSION file at the project root
        version_file = PROJECT_ROOT / "VERSION"
        try:
            return str(version_file.read_text().strip())
        except (FileNotFoundError, PermissionError):
            # Final fallback to a default version
            return "0.1.0"
