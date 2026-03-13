# Releasing the AQML VS Code Extension

## Prerequisites

- You have access to the VS Code Marketplace publisher configured in `package.json` (`aurumq` by default).
- Repository secret `VSCE_PAT` is set if you want GitHub Actions to publish automatically.
- Node.js 22+ and npm are available locally if you want to package the extension by hand.

## Local Dry Run

```bash
cd editors/vscode
npm ci
npm run package
code --install-extension ./aqml-vscode-0.3.0.vsix
```

`vsce` runs `vscode:prepublish` automatically, so the bundled AQML schema is refreshed from `spec/schema.json` before packaging.

## GitHub Actions

- `vscode-extension.yml` packages a `.vsix` on PRs, pushes to `main`, and manual dispatch.
- `publish-vscode-extension.yml` packages on tags named `vscode-v*` and publishes to the Marketplace when `VSCE_PAT` is present.

## Release Steps

1. Update `editors/vscode/package.json` version.
2. Update `editors/vscode/CHANGELOG.md`.
3. Commit the release changes.
4. Push a tag such as `vscode-v0.3.0`.

```bash
git tag vscode-v0.3.0
git push origin vscode-v0.3.0
```

If `VSCE_PAT` is not configured, the publish workflow will still build the `.vsix` and upload it as a workflow artifact.

## Manual Publish

```bash
cd editors/vscode
npm ci
npm run deploy
```

`vsce` reads the Marketplace token from `VSCE_PAT`.
