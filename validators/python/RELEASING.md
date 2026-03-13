# Releasing `aqml-validator`

This document describes the packaging and release flow for the Python validator.

## Local Preflight

Run these from the repository root:

```bash
pip install -e ".[dev]"
pytest -q
ruff check src tests
ruff format --check src tests
python -m build
twine check dist/*
```

Expected artifacts:

- `dist/aqml_validator-<version>.tar.gz`
- `dist/aqml_validator-<version>-py3-none-any.whl`

## Version Bump

1. Update `version` in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Commit the release prep changes

## GitHub Actions

### CI

Workflow: `.github/workflows/python-validator.yml`

It runs on pushes to `main` and pull requests that touch the validator package, examples, or schema.

Checks:

- `pytest -q`
- `ruff check src tests`
- `ruff format --check src tests`
- `python -m build`
- `twine check dist/*`

### Publishing

Workflow: `.github/workflows/publish-python-validator.yml`

Supported flows:

- Manual publish to TestPyPI via `workflow_dispatch`
- Manual publish to PyPI via `workflow_dispatch`
- Automatic publish to PyPI when pushing a tag matching `validator-v*`

Required repository secrets:

- `TEST_PYPI_API_TOKEN`
- `PYPI_API_TOKEN`

## Recommended Release Order

1. Publish to TestPyPI from the workflow dispatch UI
2. Create a clean virtualenv and install from TestPyPI
3. Smoke test:

```bash
pip install -i https://test.pypi.org/simple/ aqml-validator
aqml validate examples/simple-rsi.aqml
```

4. Push a release tag:

```bash
git tag validator-v0.1.0
git push origin validator-v0.1.0
```

That tag triggers the PyPI publish job.
