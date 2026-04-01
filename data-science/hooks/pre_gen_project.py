import re
import sys

def validate_python_version():
    """Verify that the provided python version matches the expected format"""
    version = "{{ cookiecutter.python_version }}"
    if not re.match(r'^\d+\.\d+\.\d+$', version):
        print(f"\033[91mERROR: Invalid Python version format: '{version}'. Expected format: X.Y.Z (e.g., 3.12.0)\033[0m")
        sys.exit(1)

def creation_note():
    print("""

===============================================================================
*** NOTE ***

To use the legacy template of Cookiecutter in case of v2, you will need
to explicitly use `-c v1` to select it.

For example:
    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
===============================================================================

    """)

# Main : Execute all the functions
validate_python_version()
creation_note()
