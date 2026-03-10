import os
from pathlib import Path
import shutil
import subprocess
from cookiecutter.main import cookiecutter as cc

def init_git():
    print("Init the git repo")
    subprocess.run(['git', 'init', '--initial-branch=main'], check=True)
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'initial commit'], check=True)

def remove_licence():
    print("")
    print("Remove LICENSE if 'No license file'")
    if "{{ cookiecutter.open_source_license }}" == "No license file":
        Path("LICENSE").unlink()

def remove_precommit():
    print("")
    if "{{ cookiecutter.install_precommit }}" == "no":
        print("Remove .pre-commit-config.yaml as requested")
        precommit_file = Path(".pre-commit-config.yaml")
        if precommit_file.exists():
            precommit_file.unlink()

def generate_nested_project():
    """Generate the Sphinx documentation with presets"""
    try:
        child_config = {
            'project_name': "{{ cookiecutter.project_name }} Documentation",
            'repo_name': "{{ cookiecutter.package_name }}",
            'author_name': "Astrodata",
            'description': "Project documentation",
            'open_source_license': "No license file",
            'sphinx_theme': "furo",
            'python_interpreter': "python3"
        }

        cc(
            "https://github.com/malganis35/cookiecutter-astrodata-squeleton.git",
            directory="sphinx-docs",
            extra_context=child_config,
            output_dir=os.path.join(os.getcwd(), "docs"),
            no_input=True,
            overwrite_if_exists=True
        )
        print("\n✅ Documentation generated successfully in the docs/ folder\n")

    except Exception as e:
        print(f"\033[91mERROR: {str(e)}\033[0m")
        if os.path.exists("docs"):
            shutil.rmtree("docs")
        raise
    
def initiate_docs():
    print("")
    print("Initiate Sphinx documentation if yes")
    if "{{ cookiecutter.initialize_sphinx_documentation }}" == "yes":
        print("Init Sphinx doc")
        generate_nested_project()
        
def ending_note():
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

# Main : Execute all the functions
remove_licence()
remove_precommit()
initiate_docs()
init_git()
ending_note()