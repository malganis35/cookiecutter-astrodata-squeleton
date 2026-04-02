"""Core utilities for path management and project structure."""

from .paths import (
    PROJECT_ROOT,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    ensure_dirs_exist
)

__all__ = ["PROJECT_ROOT", "DATA_DIR", "RAW_DATA_DIR", "PROCESSED_DATA_DIR", "MODELS_DIR", "ensure_dirs_exist"]
