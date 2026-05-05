"""
Post-generation Cookiecutter hook.

This script executes immediately after the template files have been generated.
It handles cleanup tasks (removing unused configuration files), initializing
external sub-projects (like Sphinx documentation), setting up the Git 
repository, and printing a final informative message for the user.
"""

import json
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

def copy_env_file():
    """Initialize the .env file."""
    print("Copying .env file")
    subprocess.run(['cp', '.env.example', '.env'], check=True)

# Mapping of human-readable color theme names to VSCode hex color codes
VSCODE_COLOR_MAP = {
    "Purple": "#4e29a7",
    "Blue": "#1a4fa3",
    "Teal": "#0d7377",
    "Orange": "#b85c00",
    "Red": "#a01c1c",
}

def apply_vscode_color_theme():
    """Apply the chosen VSCode color theme to .vscode/settings.json.

    Replaces the Cookiecutter placeholder with the actual hex value,
    or removes the workbench.colorCustomizations block entirely when
    the user selects 'Default (no color)'.
    """
    print("")
    print("Apply VSCode color theme")
    theme = "{{ cookiecutter.vscode_color_theme }}"
    settings_path = Path(".vscode") / "settings.json"

    if not settings_path.exists():
        return

    with settings_path.open("r", encoding="utf-8") as f:
        settings = json.load(f)

    if theme == "Default (no color)":
        settings.pop("workbench.colorCustomizations", None)
        print("  ✓ No color customization applied (Default)")
    else:
        hex_color = VSCODE_COLOR_MAP.get(theme, "#4e29a7")
        color_block = settings.get("workbench.colorCustomizations", {})
        for key in color_block:
            color_block[key] = hex_color
        settings["workbench.colorCustomizations"] = color_block
        print(f"  ✓ VSCode color theme set to {theme} ({hex_color})")

    with settings_path.open("w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

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
        # Use a -docs suffix to avoid uv workspace name conflicts with the
        # root package (both pyproject.toml would otherwise share the same name).
        # Underscores are replaced with hyphens to follow PEP 508 conventions.
        docs_repo_name = "{{ cookiecutter.package_name }}".replace("_", "-") + "-docs"
        child_config = {
            'project_name': "{{ cookiecutter.project_name }} Documentation",
            'repo_name': docs_repo_name,
            'author_name': "{{ cookiecutter.author_name }}",
            'author_email': "{{ cookiecutter.author_email }}",
            'description': "Project documentation",
            'open_source_license': "{{ cookiecutter.open_source_license }}",
            'sphinx_theme': "furo",
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
        destination = os.path.join(os.getcwd(), "docs", "project_documentation")
        
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        
        print("\n✅ Documentation generated successfully in the docs/project_documentation/ folder\n")

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
    
def remove_docs_ci():
    """Remove documentation CI/CD files if the user opted out of Sphinx documentation."""
    print("")
    if "{{ cookiecutter.initialize_sphinx_documentation }}" == "no":
        print("Remove documentation CI/CD files (Sphinx doc not requested)")
        # GitHub Actions workflow for documentation
        github_doc_workflow = Path(".github") / "workflows" / "documentation.yaml"
        if github_doc_workflow.exists():
            github_doc_workflow.unlink()
            print(f"  ✓ Removed {github_doc_workflow}")

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
3. Init the Sphinx doc in the ./docs/project_documentation/ folder (if you chose yes)
4. Use `make install` or `make dev-install` to setup the project
5. Start your project and put your *.py files in the `./src/{{ cookiecutter.package_name }}` folder.

===============================================================================
    """)

def main():
    """Run all post-generation hook tasks in order."""
    remove_licence()
    remove_precommit()
    apply_vscode_color_theme()
    initiate_docs()
    remove_docs_ci()
    init_git()
    copy_env_file()
    ending_note()


if __name__ == "__main__":
    main()