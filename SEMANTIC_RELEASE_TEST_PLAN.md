# Semantic Release Test Plan - UPDATED

## ✅ Current Status

### Fixed Issues:
- [x] Dry-run command: Use `--noop` instead of `--dry-run`
- [x] PyPI Token: Updated workflow to use your existing PYPI_API_TOKEN
- [x] Old workflow: Removed publish.yml to prevent conflicts
- [x] Build process: Verified working with hatchling

## 🧪 Testing Commands

### 1. Test Semantic Release (No-Op Mode)
```bash
cd "c:\Users\Herck\GitHub Repos\mvn-tree-visualizer"

# Test what would happen on master branch (simulated)
git checkout master
git pull origin master
uv run semantic-release --noop version

# Go back to develop
git checkout develop
```

### 2. Test Build Process
```bash
# Clean previous builds
del dist\*.* /Q

# Test build
uv run python -m build

# Verify files created
dir dist
```

### 3. Test Local Installation
```bash
# Install from built package
uv run pip install dist\mvn_tree_visualizer-1.3.0-py3-none-any.whl --force-reinstall

# Test CLI
uv run mvn-tree-visualizer --help
```

## 🚀 Safe Testing Strategy

### Option 1: Test with Small Change (Recommended)

1. **Create test feature branch:**
```bash
git checkout develop
git checkout -b test/semantic-release
```

2. **Make small documentation change:**
```bash
# Edit README.md - add a small note about automated releases
git add README.md
git commit -m "docs: add note about automated releases"
git push origin test/semantic-release
```

3. **Create PR to develop:**
- Create PR from `test/semantic-release` to `develop`
- Merge when ready

4. **Test the release process:**
```bash
git checkout develop
git pull origin develop
git checkout master
git pull origin master
git merge develop
git push origin master
```

5. **Monitor the automation:**
- Watch: https://github.com/dyka3773/mvn-tree-visualizer/actions
- Check: PyPI for new version
- Verify: GitHub releases

### Option 2: Direct Test (If You're Feeling Confident)

1. **Create a feature with conventional commit:**
```bash
git checkout develop
git checkout -b feature/improve-readme
# Make changes
git commit -m "docs: improve installation instructions"
git push origin feature/improve-readme
```

2. **Merge to develop, then master:**
```bash
# Create PR to develop, merge
# Then create PR from develop to master, merge
```

## 📋 What Will Happen

When you push to master with conventional commits:

1. **GitHub Actions will:**
   - Check out code
   - Install dependencies with uv
   - Run tests (`uv run pytest tests/ -v`)
   - Run linting (`uv run ruff check .`)
   - Analyze commits since last release
   - Determine version bump based on commit types
   - Update version in pyproject.toml
   - Generate/update CHANGELOG.md
   - Create Git tag
   - Build package (`python -m build`)
   - Upload to PyPI using your PYPI_API_TOKEN
   - Create GitHub release with auto-generated notes

2. **Expected Results:**
   - New version on PyPI
   - New Git tag
   - Updated CHANGELOG.md
   - GitHub release with notes

## 🔍 Commit Types & Version Impacts

```bash
docs: update README                    # No version change
style: fix formatting                  # No version change  
refactor: improve code structure       # No version change
test: add new test cases              # No version change
chore: update dependencies            # No version change

fix: resolve parsing error            # 1.3.0 → 1.3.1 (patch)
perf: improve performance             # 1.3.0 → 1.3.1 (patch)

feat: add theme support               # 1.3.0 → 1.4.0 (minor)

feat!: change CLI interface           # 1.3.0 → 2.0.0 (major)
# OR commit with "BREAKING CHANGE:" in body
```

## 🛡️ Safety Checks

### Before Testing:
- [x] All tests pass: `uv run pytest tests/ -v`
- [x] No lint errors: `uv run ruff check .`
- [x] Build works: `uv run python -m build`
- [x] PYPI_API_TOKEN is set in GitHub repository secrets

### During Testing:
- Monitor GitHub Actions in real-time
- Check for any error messages
- Verify each step completes successfully

### After Testing:
- Confirm new version appears on PyPI
- Test installation: `pip install mvn-tree-visualizer`
- Verify CLI works: `mvn-tree-visualizer --help`

## 🆘 Rollback Plan

If something goes wrong:

1. **Failed build/tests:** Fix the issue and make another commit
2. **Wrong version bump:** Make a new commit with correct conventional format
3. **PyPI upload fails:** Check token, manually upload if needed
4. **Complete disaster:** Revert to manual process temporarily

## Ready to Test?

The safest approach is **Option 1** with a documentation change. This will:
- Test the entire pipeline
- Create minimal risk (docs-only change)
- Let you see how everything works
- Build confidence for future releases

Would you like to proceed with Option 1?
