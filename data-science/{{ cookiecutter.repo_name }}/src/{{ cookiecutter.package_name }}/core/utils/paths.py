"""Centralized path management to avoid relative path hell."""

from pathlib import Path


def _find_project_root() -> Path:
    """Find the project root dynamically by looking for pyproject.toml."""
    current_dir = Path(__file__).resolve().parent
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / "pyproject.toml").exists():
            return parent
    # Fallback to the default structure if not found
    return Path(__file__).resolve().parents[4]


PROJECT_ROOT: Path = _find_project_root()

# Data directories
DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DATA_DIR: Path = DATA_DIR / "raw"
INTERIM_DATA_DIR: Path = DATA_DIR / "interim"
PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
EXTERNAL_DATA_DIR: Path = DATA_DIR / "external"

# Models directory
MODELS_DIR: Path = PROJECT_ROOT / "models"

# Notebooks directory
NOTEBOOKS_DIR: Path = PROJECT_ROOT / "notebooks"

# Logs directory
LOGS_DIR: Path = PROJECT_ROOT / "logs"


def ensure_dirs_exist() -> None:
    """Create directories if they don't exist."""
    for dir_path in [RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR, EXTERNAL_DATA_DIR, MODELS_DIR, LOGS_DIR]:
        dir_path.mkdir(parents=True, exist_ok=True)
