import os
from pathlib import Path

def remove_licence():
    """Remove the LICENSE file if the user opted out of open source licensing."""
    if "{{ cookiecutter.open_source_license }}" == "No license file":
        license_file = Path("LICENSE")
        if license_file.exists():
            license_file.unlink()

def main():
    remove_licence()

if __name__ == "__main__":
    main()
