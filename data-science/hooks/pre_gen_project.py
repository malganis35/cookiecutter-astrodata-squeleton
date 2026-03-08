#%% Define functions
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
creation_note()
