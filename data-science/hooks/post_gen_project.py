"""
Post-generation Cookiecutter hook.

This script executes immediately after the template files have been generated.
It handles cleanup tasks (removing unused configuration files), initializing
external sub-projects (like Sphinx documentation), setting up the Git 
repository, and printing a final informative message for the user.
"""

import os
from pathlib import Path
import subprocess
from cookiecutter.main import cookiecutter as cc

def init_git():
    """Initialize a git repository in the generated project and make the first commit."""
    print("Init the git repo")
    subprocess.run(['git', 'init', '--initial-branch=main'], check=True)
    subprocess.run(['uv', 'sync'], check=True)
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'initial commit'], check=True)

def remove_licence():
    """Remove the LICENSE file if the user opted out of open source licensing."""
    print("")
    print("Remove LICENSE if 'No license file'")
    if "{{ cookiecutter.open_source_license }}" == "No license file":
        Path("LICENSE").unlink()

def remove_precommit():
    """Remove the .pre-commit-config.yaml file if the user opted out of pre-commit."""
    print("")
    if "{{ cookiecutter.install_precommit }}" == "no":
        print("Remove .pre-commit-config.yaml as requested")
        precommit_file = Path(".pre-commit-config.yaml")
        if precommit_file.exists():
            precommit_file.unlink()

def generate_nested_project():
    """Generate the Sphinx documentation with presets"""
    from cookiecutter.exceptions import CookiecutterException
    import tempfile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    try:
        child_config = {
            'project_name': "{{ cookiecutter.project_name }} Documentation",
            'repo_name': "{{ cookiecutter.package_name }}",
            'author_name': "{{ cookiecutter.author_name }}",
            'author_email': "{{ cookiecutter.author_email }}",
            'description': "Project documentation",
            'open_source_license': "{{ cookiecutter.open_source_license }}",
            'sphinx_theme': "furo",
            'python_interpreter': "{{ cookiecutter.python_interpreter }}"
        }

        cc(
            "https://github.com/malganis35/cookiecutter-astrodata-squeleton.git",
            directory="sphinx-docs",
            extra_context=child_config,
            output_dir=temp_dir,
            no_input=True,
            overwrite_if_exists=True
        )
        
        source = os.path.join(temp_dir, child_config['repo_name'])
        destination = os.path.join(os.getcwd(), "docs")
        
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        
        print("\n✅ Documentation generated successfully in the docs/ folder\n")

    except CookiecutterException as e:
        print(f"\033[91mERROR: Failed to generate documentation: {e}\033[0m")
        print("You can generate it manually later with: make docs")
    except subprocess.CalledProcessError as e:
        print(f"\033[91mERROR: Command failed: {e.cmd}\033[0m")
    except Exception as e:
        print(f"\033[91mUNEXPECTED ERROR: {e}\033[0m")
        raise
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    
def initiate_docs():
    """Determine whether to generate the nested Sphinx documentation based on user input."""
    print("")
    print("Initiate Sphinx documentation if yes")
    if "{{ cookiecutter.initialize_sphinx_documentation }}" == "yes":
        print("Init Sphinx doc")
        generate_nested_project()
        
def ending_note():
    """Print helpful instructions and next steps after successful project generation."""
    print("""
===============================================================================
*** END NOTE ***

AstroData Squeleton is finished:
1. Project folder structure is initialized
2. Git repo is initialized on main branch
3. First initial commit is created

Next Steps:
1. Navigate to your new project
2. Create a repo on Gitlab/Github and push the code
3. Init the Sphinx doc in the ./docs/ folder (if you chose yes)
4. Use `make install` or `make dev-install` to setup the project
5. Start your project and put your *.py files in the `./src/{{ cookiecutter.package_name }}` folder.

===============================================================================
    """)

def main():
    """Run all post-generation hook tasks in order."""
    remove_licence()
    remove_precommit()
    initiate_docs()
    init_git()
    ending_note()


if __name__ == "__main__":
    main()