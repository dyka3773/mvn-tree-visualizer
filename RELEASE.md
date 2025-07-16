# Release Procedure

This document describes the step-by-step process for releasing a new version of `mvn-tree-visualizer` to PyPI.

## Overview

The project follows a GitFlow-like workflow with the following branches:
- `develop` - Active development branch where features are integrated
- `master` - Protected production branch, only updated for releases
- `feature/*` - Individual feature branches

Releases are automatically published to PyPI when code is pushed to the `master` branch via GitHub Actions.

## Prerequisites

Before starting a release, ensure you have:
- [ ] Maintainer access to the repository
- [ ] All planned features for the release completed and merged into `develop`
- [ ] All tests passing on the `develop` branch
- [ ] No outstanding critical issues

## Release Process

### 1. Prepare the Release Branch

```bash
# Ensure you're on the latest develop branch
git checkout develop
git pull origin develop

# Create a release preparation branch
git checkout -b release/prepare-v1.x.x
```

### 2. Update Version and Documentation

#### Update Version Number
Edit `pyproject.toml` and update the version number:
```toml
[project]
name = "mvn-tree-visualizer"
version = "1.x.x"  # Update this line
```

#### Update CHANGELOG.md
1. Move items from `[Unreleased]` section to a new version section
2. Add the release date
3. Ensure all changes are properly categorized (Added, Changed, Fixed, Removed)
4. Add a new empty `[Unreleased]` section for future changes

Example:
```markdown
## [Unreleased]

### Added
- Placeholder for future features

## [1.x.x] - 2025-MM-DD

### Added
- New feature descriptions

### Changed
- Modified functionality descriptions

### Fixed
- Bug fix descriptions
```

#### Update CONTEXT.md
1. Move the current version from "Completed Tasks" to "Previous Releases"
2. Update the "Current Status" section for the next version
3. Update any relevant project information

#### Update the SECURITY.md
1. Review and update the security policy if necessary
2. Ensure it reflects the current security practices and reporting procedures
3. Add any new security features or changes made in this release

### 3. Quality Assurance

Run the complete test suite and quality checks:

```bash
# Run all tests
uv run pytest tests/ -v

# Run linting
uv run ruff check .

# Test the CLI locally
uv run mvn-tree-visualizer --help

# Test with example data
cd examples/simple-project
uv run mvn-tree-visualizer --filename maven_dependency_file --output test-diagram.html
```

Verify that:
- [ ] All 22+ tests pass
- [ ] No linting errors
- [ ] CLI commands work as expected
- [ ] Example outputs generate correctly

### 4. Create Release Pull Request

```bash
# Commit the version updates
git add pyproject.toml CHANGELOG.md CONTEXT.md SECURITY.md
git commit -m "Prepare release v1.x.x

- Update version to 1.x.x in pyproject.toml
- Update CHANGELOG.md with release notes
- Update CONTEXT.md with current status
- Update SECURITY.md with current security practices"
```

# Push the release preparation branch
```bash
git push origin release/prepare-v1.x.x
```

Create a pull request from `release/prepare-v1.x.x` to `develop` with:
- Title: "Prepare release v1.x.x"
- Description summarizing the changes in this release
- Link to any relevant issues or PRs

### 5. Merge to Develop

Once the release preparation PR is reviewed and approved:
1. Merge the PR into `develop`
2. Delete the release preparation branch

### 6. Create Release PR to Master

```bash
# Create a pull request from develop to master
git checkout develop
git pull origin develop
```

Create a pull request from `develop` to `master` with:
- Title: "Release v1.x.x"
- Description: Copy the changelog entry for this version
- Reference the milestone or project board if applicable

### 7. Final Release

Once the release PR is approved:

1. **Merge to Master**: Merge the PR to `master` (this triggers automatic PyPI publication)

2. **Create Git Tag**: After the merge, create and push a git tag:
```bash
git checkout master
git pull origin master
git tag -a v1.x.x -m "Release version 1.x.x"
git push origin v1.x.x
```

3. **Monitor Deployment**: Check the [GitHub Actions](https://github.com/dyka3773/mvn-tree-visualizer/actions) to ensure:
   - [ ] Tests pass
   - [ ] Package builds successfully  
   - [ ] PyPI upload completes without errors

4. **Verify PyPI Release**: Check [PyPI](https://pypi.org/project/mvn-tree-visualizer/) to confirm the new version is available

5. **Create GitHub Release**: Create a release on GitHub with:
   - Tag: `v1.x.x`
   - Title: `v1.x.x`
   - Description: Copy from CHANGELOG.md
   - Mark as latest release

## Post-Release Tasks

### Update Documentation
- [ ] Verify README.md installation instructions work with new version
- [ ] Update any version-specific documentation
- [ ] Check that examples still work with the new version

### Cleanup
```bash
# Clean up any local release branches
git branch -d release/prepare-v1.x.x

# Switch back to develop for future work
git checkout develop
git pull origin develop
```

## Emergency Hotfixes

For critical bugs that need immediate fixes:

1. Create a hotfix branch from `master`: `git checkout -b hotfix/fix-critical-bug master`
2. Make the minimal necessary changes
3. Update version number (patch version increment)
4. Update CHANGELOG.md
5. Create PR to both `master` and `develop`
6. Follow the same release process

## Troubleshooting

### Failed PyPI Upload
- Check GitHub Actions logs for specific error messages
- Verify PyPI API token is still valid
- Ensure version number hasn't been used before
- Check that all required files are included in the build

### Failed Tests
- Do not proceed with release if any tests fail
- Fix issues on the `develop` branch first
- Re-run the release process from step 1

### Version Conflicts
- Ensure version in `pyproject.toml` follows semantic versioning
- Check that the version doesn't already exist on PyPI
- Verify version is higher than the current latest version

## Rollback Procedure

If a release needs to be rolled back:

1. **Immediate**: If possible, fix forward with a patch release
2. **PyPI**: Contact PyPI support to remove a problematic version (rarely needed)
3. **Documentation**: Update README and docs to recommend the previous stable version
4. **Git**: Create a new release with the previous stable code if necessary

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR** (1.x.x): Breaking changes, major new features
- **MINOR** (x.1.x): New features, backward compatible
- **PATCH** (x.x.1): Bug fixes, backward compatible

Examples:
- `1.0.0` → `1.0.1` (bug fix)
- `1.0.1` → `1.1.0` (new feature)
- `1.1.0` → `2.0.0` (breaking change)
