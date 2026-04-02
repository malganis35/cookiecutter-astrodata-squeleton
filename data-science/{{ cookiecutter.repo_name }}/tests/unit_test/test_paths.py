"""Unit tests for project path utilities."""

from pathlib import Path

import pytest

from {{ cookiecutter.package_name }}.core.utils import paths


def test_ensure_dirs_exist(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that ensure_dirs_exist creates the physical directories correctly.

    Uses pytest's tmp_path fixture to avoid polluting the actual file system.
    """
    # Override the module-level constants with our temporary paths
    monkeypatch.setattr(paths, "RAW_DATA_DIR", tmp_path / "data" / "raw")
    monkeypatch.setattr(paths, "INTERIM_DATA_DIR", tmp_path / "data" / "interim")
    monkeypatch.setattr(paths, "PROCESSED_DATA_DIR", tmp_path / "data" / "processed")
    monkeypatch.setattr(paths, "EXTERNAL_DATA_DIR", tmp_path / "data" / "external")
    monkeypatch.setattr(paths, "MODELS_DIR", tmp_path / "models")
    monkeypatch.setattr(paths, "LOGS_DIR", tmp_path / "logs")

    # Ensure they don't exist prior to calling the function
    assert not (tmp_path / "data" / "raw").exists()
    assert not (tmp_path / "logs").exists()

    # Execute the function
    paths.ensure_dirs_exist()

    # Verify that all directories were physically created
    assert (tmp_path / "data" / "raw").exists()
    assert (tmp_path / "data" / "interim").exists()
    assert (tmp_path / "data" / "processed").exists()
    assert (tmp_path / "data" / "external").exists()
    assert (tmp_path / "models").exists()
    assert (tmp_path / "logs").exists()

    # Calling it a second time should not raise an error (exist_ok=True)
    try:
        paths.ensure_dirs_exist()
    except FileExistsError:
        pytest.fail("ensure_dirs_exist raised FileExistsError unexpectedly on second call.")


def test_find_project_root_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that _find_project_root falls back when no pyproject.toml is found.

    Mocks Path.exists to always return False, forcing the fallback return on line 13.
    """
    original_exists = Path.exists

    def fake_exists(self: Path) -> bool:
        if self.name == "pyproject.toml":
            return False
        return original_exists(self)

    monkeypatch.setattr(Path, "exists", fake_exists)

    result = paths._find_project_root()
    # The fallback should return a valid Path (parents[4] from __file__)
    assert isinstance(result, Path)
