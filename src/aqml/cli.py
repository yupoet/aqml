"""CLI entrypoints for AQML validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from aqml.loader import normalize
from aqml.schema import schema_path
from aqml.validator import parse, validate


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aqml", description="AQML v2 validator and formatter")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate one or more AQML files")
    validate_parser.add_argument("paths", nargs="+", help="AQML files to validate")
    validate_parser.add_argument("--json", action="store_true", help="Emit JSON results")

    normalize_parser = subparsers.add_parser("normalize", help="Normalize AQML formatting")
    normalize_parser.add_argument("path", help="AQML file to normalize")
    normalize_parser.add_argument(
        "-o", "--output", help="Write output to this path instead of stdout"
    )
    normalize_parser.add_argument(
        "--in-place", action="store_true", help="Overwrite the input file"
    )

    parse_parser = subparsers.add_parser("parse", help="Parse AQML and print JSON")
    parse_parser.add_argument("path", help="AQML file to parse")

    subparsers.add_parser("schema-path", help="Print the bundled JSON Schema path")
    return parser


def _command_validate(paths: list[str], as_json: bool) -> int:
    overall_ok = True
    payload = []

    for path in paths:
        result = validate(Path(path))
        if as_json:
            payload.append(
                {
                    "path": path,
                    "valid": result.valid,
                    "errors": [
                        {"path": issue.path, "message": issue.message, "level": issue.level}
                        for issue in result.errors
                    ],
                    "warnings": [
                        {"path": issue.path, "message": issue.message, "level": issue.level}
                        for issue in result.warnings
                    ],
                }
            )
        else:
            if result.valid:
                print(f"OK {path}")
            else:
                overall_ok = False
                print(f"ERROR {path}")
                for issue in result.errors:
                    print(f"  - {issue.path}: {issue.message}")

    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        overall_ok = all(item["valid"] for item in payload)

    return 0 if overall_ok else 1


def _command_normalize(path: str, output: str | None, in_place: bool) -> int:
    normalized = normalize(Path(path))

    if in_place:
        Path(path).write_text(normalized, encoding="utf-8")
        print(path)
        return 0

    if output:
        Path(output).write_text(normalized, encoding="utf-8")
        print(output)
        return 0

    print(normalized, end="")
    return 0


def _command_parse(path: str) -> int:
    print(json.dumps(parse(Path(path)), ensure_ascii=False, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the AQML CLI."""

    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate":
        return _command_validate(args.paths, args.json)
    if args.command == "normalize":
        return _command_normalize(args.path, args.output, args.in_place)
    if args.command == "parse":
        return _command_parse(args.path)
    if args.command == "schema-path":
        print(schema_path())
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2
