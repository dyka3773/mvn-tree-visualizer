# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [v1.8.4](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.8.4) - 2025-11-24

<small>[Compare with v1.8.3](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.8.3...v1.8.4)</small>

## [v1.8.3](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.8.3) - 2025-11-24

<small>[Compare with v1.8.2](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.8.2...v1.8.3)</small>

## [v1.8.2](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.8.2) - 2025-11-10

<small>[Compare with v1.8.1](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.8.1...v1.8.2)</small>

## [v1.8.1](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.8.1) - 2025-11-10

<small>[Compare with v1.8.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.8.0...v1.8.1)</small>

## [v1.8.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.8.0) - 2025-08-13

<small>[Compare with v1.7.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.7.0...v1.8.0)</small>

### Features

- add --timestamp-output flag to append timestamp to output filenames ([0292ac5](https://github.com/dyka3773/mvn-tree-visualizer/commit/0292ac5209a6b16c281b8146acc32e47264a02a7) by Hercules Konsoulas).
- add --open flag to automatically open HTML diagrams in browser ([fb5237e](https://github.com/dyka3773/mvn-tree-visualizer/commit/fb5237ee5e3696bd550b08c1d8a4d5b428666b6f) by Hercules Konsoulas).

### Code Refactoring

- encode URL with proper built-in function ([eed841d](https://github.com/dyka3773/mvn-tree-visualizer/commit/eed841d007f1d2a0b0d6632d8a36b93e4524acc2) by Hercules Konsoulas).
- restructure test suite into modular architecture ([6d25b7b](https://github.com/dyka3773/mvn-tree-visualizer/commit/6d25b7b1948252615d32ff7076428dc520ed60de) by Hercules Konsoulas).
- moved timestamp creation to a separate util module for clarity ([cf8d188](https://github.com/dyka3773/mvn-tree-visualizer/commit/cf8d1885b0a4056988dba94496a4ac992af2b693) by Hercules Konsoulas).

## [v1.7.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.7.0) - 2025-08-02

<small>[Compare with v1.6.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.6.0...v1.7.0)</small>

### Features

- add --quiet/-q flag for silent operation ([5dfc82c](https://github.com/dyka3773/mvn-tree-visualizer/commit/5dfc82c57987870ab6200a7ec6682bda3aaf06c7) by Hercules Konsoulas).
- add --version/-v flag to display current tool version ([6ee3e56](https://github.com/dyka3773/mvn-tree-visualizer/commit/6ee3e56302893aecb5ad87c115ea801acf03b4bc) by Hercules Konsoulas).

### Bug Fixes

- CLI test timeouts and file cleanup issues ([3d236d9](https://github.com/dyka3773/mvn-tree-visualizer/commit/3d236d93406e4bcc0a0ee6ea4c6f096ba5c0f861) by Hercules Konsoulas).

### Code Refactoring

- correct copilot's mistake for traceback ([d33b5a8](https://github.com/dyka3773/mvn-tree-visualizer/commit/d33b5a847399b34cb101f5650ff98af29e133db1) by Hercules Konsoulas).

## [v1.6.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.6.0) - 2025-07-24

<small>[Compare with v1.5.2](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.5.2...v1.6.0)</small>

### Features

- add beta release support for develop branch ([e578499](https://github.com/dyka3773/mvn-tree-visualizer/commit/e5784991ae136242fd4c8ddb929704f2b6f77616) by Hercules Konsoulas).

### Bug Fixes

- implement comprehensive changelog generation with git-changelog ([17e0c89](https://github.com/dyka3773/mvn-tree-visualizer/commit/17e0c894dfaff23ab464be52c9e1df8ac4bf71bc) by Hercules Konsoulas).

## [v1.5.2](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.5.2) - 2025-07-24

<small>[Compare with v1.5.1](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.5.1...v1.5.2)</small>

### Bug Fixes

- enable automatic changelog generation in semantic release ([c10460e](https://github.com/dyka3773/mvn-tree-visualizer/commit/c10460e09e96510ae95e795dafae53ac28230c50) by Hercules Konsoulas).

## [v1.5.1](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.5.1) - 2025-07-21

<small>[Compare with v1.5.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.5.0...v1.5.1)</small>

### Bug Fixes

- resolve an issue causing similar duplicate logs ([e861008](https://github.com/dyka3773/mvn-tree-visualizer/commit/e86100867de380ea37ff49a8b4d4659486bd7046) by Hercules Konsoulas).

### Code Refactoring

- remove unused and wrong imports ([3051ea2](https://github.com/dyka3773/mvn-tree-visualizer/commit/3051ea20b9f40f40c97a5b3aed5a67c167b75a99) by Hercules Konsoulas).

## [v1.5.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.5.0) - 2025-07-19

<small>[Compare with v1.4.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.4.0...v1.5.0)</small>

### Features

- resolve GitHub issue #7 with enhanced large project support ([3b3b14e](https://github.com/dyka3773/mvn-tree-visualizer/commit/3b3b14e88608c4b1c64295bbf786a898e3b600be) by Hercules Konsoulas).

### Code Refactoring

- updated another test to stay consistent with the previous commits ([01a100f](https://github.com/dyka3773/mvn-tree-visualizer/commit/01a100f01587a3f2b43eaa9b6859d7c77e849202) by Hercules Konsoulas).
- centralize all magic numbers into shared constants module ([e3ee53c](https://github.com/dyka3773/mvn-tree-visualizer/commit/e3ee53cd99f146ca56265ea54c1ea3389ee1e1d8) by Hercules Konsoulas).
- extract hardcoded magic numbers to named constants ([f1f6734](https://github.com/dyka3773/mvn-tree-visualizer/commit/f1f67347b401959d1700e2da36632e1eb87e6a34) by Hercules Konsoulas).
- fix to previous commit ([2652892](https://github.com/dyka3773/mvn-tree-visualizer/commit/265289286eafe94f3aeef649ed6856c587061941) by Hercules Konsoulas).
- extract zoom configuration values to constants ([b2d506e](https://github.com/dyka3773/mvn-tree-visualizer/commit/b2d506e7446e79e998be3bc6bd000930a7cab78c) by Hercules Konsoulas).

## [v1.4.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.4.0) - 2025-07-17

<small>[Compare with v1.3.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.3.0...v1.4.0)</small>

### Features

- add theme system with minimal and dark themes ([649e317](https://github.com/dyka3773/mvn-tree-visualizer/commit/649e317dac9531cc16b03cba3602994188468bf9) by Hercules Konsoulas).

## [v1.3.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.3.0) - 2025-07-16

<small>[Compare with v1.2.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.2.0...v1.3.0)</small>

### Features

- implement automated release system ([e8fc847](https://github.com/dyka3773/mvn-tree-visualizer/commit/e8fc8472ecbc3ebc7376b07f43aae63a27f299bc) by Hercules Konsoulas).
- implement v1.3.0 user experience improvements ([2b87699](https://github.com/dyka3773/mvn-tree-visualizer/commit/2b8769903c34527542ee491ea9ac58f46e439e23) by Hercules Konsoulas).
- enhance error handling and refactor code organization ([c4a183c](https://github.com/dyka3773/mvn-tree-visualizer/commit/c4a183c59380c30d6fe74e8609fc5eb706e88c85) by Hercules Konsoulas).
- transform repository into professional open-source project ([4ceebdc](https://github.com/dyka3773/mvn-tree-visualizer/commit/4ceebdc886c87eb0d9852259a3aa06d0bc610ab2) by Hercules Konsoulas).

### Bug Fixes

- install build module within semantic-release build command ([cd5718d](https://github.com/dyka3773/mvn-tree-visualizer/commit/cd5718d56cd91934b55285c46713bb6cd738b4fa) by Hercules Konsoulas).
- ensure build tools available for semantic-release action ([e2db367](https://github.com/dyka3773/mvn-tree-visualizer/commit/e2db367f3ebd14768eee5efc5d7515fab0f48c1c) by Hercules Konsoulas).
- use uv run for build command in semantic-release ([bc5857b](https://github.com/dyka3773/mvn-tree-visualizer/commit/bc5857b080224b2489542470bff9beabf84b59fa) by Hercules Konsoulas).
- add missing ruff dependency for CI linting ([675d892](https://github.com/dyka3773/mvn-tree-visualizer/commit/675d89209db91d0bbf234b7872a5a1893d81b729) by Hercules Konsoulas).
- corrected funding link ([13c76c4](https://github.com/dyka3773/mvn-tree-visualizer/commit/13c76c4ad99ead6ecb5d7471c07b5ea5a22ffc8f) by Hercules Konsoulas).
- install pytest separately in CI to resolve command not found error ([1a99192](https://github.com/dyka3773/mvn-tree-visualizer/commit/1a991927a9d94a405170d93660b62f89513e0056) by Hercules Konsoulas).
- update JSON tests to match show_versions=False default ([88bcf95](https://github.com/dyka3773/mvn-tree-visualizer/commit/88bcf951f08243c97ddf8d3f3fa4c26e3f7de41d) by Hercules Konsoulas).

### Code Refactoring

- add watch mode and standardize JSON output format ([c1a6e14](https://github.com/dyka3773/mvn-tree-visualizer/commit/c1a6e143120031b4f9cf2417cb5db32a35899ddb) by Hercules Konsoulas).

## [v1.2.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.2.0) - 2025-07-08

<small>[Compare with v1.1.0](https://github.com/dyka3773/mvn-tree-visualizer/compare/v1.1.0...v1.2.0)</small>

### Features

- add --show-versions flag for both HTML and JSON outputs ([80c7d10](https://github.com/dyka3773/mvn-tree-visualizer/commit/80c7d1089e21c3a345bdc9a61242ed1233605a0e) by Hercules Konsoulas).
- add comprehensive type hints to improve code quality ([b9b9da5](https://github.com/dyka3773/mvn-tree-visualizer/commit/b9b9da5a48b3c40feeca40de0c69eef3316afc7f) by Hercules Konsoulas).

### Bug Fixes

- Correct dependency installation in workflow ([3e500fc](https://github.com/dyka3773/mvn-tree-visualizer/commit/3e500fc76927b736a0f529ad8b2261b6735b949d) by Hercules Konsoulas).

## [v1.1.0](https://github.com/dyka3773/mvn-tree-visualizer/releases/tag/v1.1.0) - 2025-07-08

<small>[Compare with first commit](https://github.com/dyka3773/mvn-tree-visualizer/compare/58ba414323de8d69f0f80a514cf9bb14f40fa22c...v1.1.0)</small>

### Features

- Add JSON output and decouple output logic ([e6cd138](https://github.com/dyka3773/mvn-tree-visualizer/commit/e6cd13836f93221f2dbd334574ca614d7dbe0e4a) by Hercules Konsoulas).
