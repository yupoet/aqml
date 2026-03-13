from __future__ import annotations

from pathlib import Path

import yaml

from aqml.validator import validate


def test_gallery_index_matches_templates() -> None:
    gallery_dir = Path("templates/gallery")
    index = yaml.safe_load((gallery_dir / "index.yaml").read_text(encoding="utf-8"))

    listed_files = {entry["file"] for entry in index["templates"]}
    actual_files = {path.name for path in gallery_dir.glob("*.aqml")}

    assert listed_files == actual_files


def test_all_gallery_templates_validate() -> None:
    templates = sorted(Path("templates/gallery").glob("*.aqml"))
    assert templates

    for path in templates:
        result = validate(path)
        assert result.valid, f"{path}: {[f'{item.path}: {item.message}' for item in result.errors]}"
