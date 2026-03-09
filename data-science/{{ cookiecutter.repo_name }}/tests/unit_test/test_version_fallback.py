import pytest
from pathlib import Path
from unittest.mock import patch
from project_name.api.main import get_project_version as get_main_version
from project_name.api.routers.system import get_project_version as get_system_version

def test_main_version_fallback():
    """Tests the fallback version logic in main.py when VERSION file is missing or unreadable."""
    with patch("pathlib.Path.read_text") as mock_read:
        mock_read.side_effect = Exception("File not found")
        version = get_main_version()
        assert version == "0.1.0"

def test_system_version_fallback():
    """Tests the fallback version logic in routers/system.py when VERSION file is missing or unreadable."""
    with patch("pathlib.Path.read_text") as mock_read:
        mock_read.side_effect = Exception("File not found")
        version = get_system_version()
        assert version == "0.1.0"
