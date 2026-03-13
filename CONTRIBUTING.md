# Contributing to AQML

Thank you for your interest in contributing to AQML (Aurum Quant Markup Language)!

## Ways to Contribute

### 📝 Strategy Examples
Submit new strategy examples in `examples/`. Each file should:
- Use `.aqml` extension
- Include `version: "2.0"` and `signal_type`
- Have clear `name` and `description`
- Include `comment` on each top-level rule item
- Pass JSON Schema validation and AurumQ executable-profile validation

### 🐛 Spec Issues
Found an ambiguity or inconsistency in the specification? Open an issue with:
- The specific section reference
- What is unclear or inconsistent
- Your suggested clarification

### 🔧 Tooling
Build validators, IDE extensions, or parsers:
- Follow the spec strictly for validation logic
- Include test cases from `examples/`
- Document supported/unsupported features

### 🌐 Translations
Help translate documentation:
- `docs/` directory for translated guides
- Use `docs/{language_code}/` structure (e.g., `docs/zh/`, `docs/ja/`)

### 💡 Spec Extensions (RFC)
Propose new features via RFC:
1. Open an issue titled `RFC: {feature name}`
2. Describe the use case and motivation
3. Provide proposed YAML syntax
4. Include backward compatibility analysis

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-contribution`)
3. Make your changes
4. Validate any `.aqml` files against `spec/schema.json`
5. Commit with a clear message
6. Open a Pull Request

## Code of Conduct

Be respectful, constructive, and inclusive. We welcome contributors of all experience levels.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
