# Release Procedure

This document describes the automated release process for `mvn-tree-visualizer` using `python-semantic-release`.

## Overview

The project uses automated releases with **python-semantic-release**:
- **Automatic versioning** based on conventional commit messages
- **Automatic CHANGELOG.md generation** from commit history
- **Automatic PyPI publication** when code is pushed to `master`
- **Automatic GitHub releases** with release notes

### Workflow Branches:
- `develop` - Active development branch where features are integrated
- `master` - Protected production branch, triggers automated releases
- `feature/*` - Individual feature branches

## Conventional Commits

All commits must follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Commit Types and Version Impact:
- `feat:` - New feature → **MINOR** version bump (1.3.0 → 1.4.0)
- `fix:` - Bug fix → **PATCH** version bump (1.3.0 → 1.3.1)  
- `perf:` - Performance improvement → **PATCH** version bump
- `feat!:` or `BREAKING CHANGE:` → **MAJOR** version bump (1.3.0 → 2.0.0)
- `docs:`, `style:`, `refactor:`, `test:`, `chore:` - No version bump

### Examples:
```bash
feat: add theme support with --theme option
fix: resolve dependency parsing error with special characters  
feat!: change CLI interface for better usability
docs: update README with theme examples
```

## Automated Release Process

### 1. Development Workflow

```bash
# Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/add-theme-support

# Make changes and commit using conventional commits
git add .
git commit -m "feat: add theme system with dark/light modes"
git push origin feature/add-theme-support
```

### 2. Create Pull Request to Develop

Create a pull request from your feature branch to `develop`:
- Title: Clear description of the feature
- Description: Details of changes and any breaking changes
- Ensure all tests pass in CI

### 3. Merge to Develop

Once the PR is reviewed and approved, merge it into `develop`.

### 4. Release to Master

When ready for a release:

```bash
# Create release PR from develop to master
git checkout develop
git pull origin develop
```

Create a pull request from `develop` to `master`:
- Title: "Release: Prepare for next version"
- Description: Summary of changes since last release
- List any breaking changes

### 5. Automated Release (Master Branch)

When the release PR is merged to `master`, the automation triggers:

1. **python-semantic-release analyzes commits** since the last release
2. **Determines version bump** based on conventional commit types
3. **Updates version** in `pyproject.toml`
4. **Generates CHANGELOG.md** from commit messages
5. **Creates Git tag** with new version
6. **Builds package** using `python -m build`
7. **Publishes to PyPI** automatically
8. **Creates GitHub release** with generated release notes

## Monitoring Releases

### Check Release Status:
1. **GitHub Actions**: Monitor the [release workflow](https://github.com/dyka3773/mvn-tree-visualizer/actions)
2. **PyPI**: Verify new version appears on [PyPI](https://pypi.org/project/mvn-tree-visualizer/)
3. **GitHub Releases**: Check [GitHub releases page](https://github.com/dyka3773/mvn-tree-visualizer/releases)

### Troubleshooting:

**Failed Release:**
- Check GitHub Actions logs for specific errors
- Verify conventional commit format in recent commits
- Ensure GITHUB_TOKEN has sufficient permissions
- Check PyPI trusted publishing configuration

**No Version Bump:**
- Ensure commits follow conventional commit format
- Check that commits include `feat:` or `fix:` types
- Verify commits are not filtered out by semantic-release config

## Configuration

The release behavior is configured in `pyproject.toml`:

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
build_command = "python -m build"
upload_to_pypi = true
upload_to_release = true

[tool.semantic_release.commit_parser_options]
allowed_tags = ["build", "chore", "ci", "docs", "feat", "fix", "perf", "style", "refactor", "test"]
minor_tags = ["feat"]
patch_tags = ["fix", "perf"]
```

## Emergency Procedures

### Rollback a Release:
```bash
# Revert the problematic release commit
git revert <release-commit-hash>

# Push to master to trigger new patch release
git push origin master
```

### Hotfix Process:
```bash
# Create hotfix branch from master
git checkout master
git checkout -b hotfix/critical-bug-fix

# Make minimal fix
git commit -m "fix: resolve critical security vulnerability"

# Create PR directly to master (bypass develop for emergencies)
```

This automated approach ensures consistent, reliable releases while reducing manual effort and human error.
