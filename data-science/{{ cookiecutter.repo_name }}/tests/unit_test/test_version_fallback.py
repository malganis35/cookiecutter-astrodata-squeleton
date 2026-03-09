import pytest
from pathlib import Path
from unittest.mock import patch
from {{ cookiecutter.package_name }}.api.main import get_project_version

def test_main_version_fallback():
    """Tests the fallback version logic in main.py when VERSION file is missing or unreadable."""
    with patch("pathlib.Path.read_text") as mock_read:
        # On simule l'absence du fichier VERSION
        mock_read.side_effect = Exception("File not found")
        
        # On appelle la fonction de récupération de version
        version = get_project_version()
        
        # On vérifie que le fallback s'active correctement
        assert version == "0.1.0"