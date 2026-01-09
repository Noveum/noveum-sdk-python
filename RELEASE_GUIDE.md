# Release Guide for noveum-sdk-python

This guide provides step-by-step instructions for releasing a new version of the Noveum SDK to PyPI.

## Prerequisites

Before making a release, ensure:

1. ✅ All tests pass locally (unit tests)
2. ✅ Code is properly formatted and linted
3. ✅ README.md exists in the root directory
4. ✅ CHANGELOG.md is updated with release notes
5. ✅ Version in `pyproject.toml` is correct
6. ✅ All changes are committed to the `SDKImprovement` branch
7. ✅ PyPI Trusted Publishing is configured (see below)

## Current Status

- **Current Version**: 1.0.0
- **Branch**: SDKImprovement
- **Tests**: ✅ 213 unit tests passing
- **Files Ready**: 
  - ✅ README.md (added)
  - ✅ CHANGELOG.md (created)
  - ✅ setup.py (updated with type hints)

## PyPI Trusted Publishing Setup

Before your first release, you need to configure Trusted Publishing on PyPI:

### 1. Create PyPI Account (if needed)
- Go to https://pypi.org/account/register/
- Verify your email

### 2. Configure Trusted Publisher
1. Go to https://pypi.org/manage/account/publishing/
2. Click "Add a new pending publisher"
3. Fill in:
   - **PyPI Project Name**: `noveum-sdk-python`
   - **Owner**: `Noveum` (your GitHub organization/username)
   - **Repository name**: `noveum-sdk-python`
   - **Workflow name**: `release.yml`
   - **Environment name**: `pypi`
4. Click "Add"

**Note**: For the first release, you need to use "pending publisher". After the first successful release, the project will be created on PyPI automatically.

## Release Steps

### Step 1: Commit Your Changes

```bash
cd /Users/mramanindia/work/noveum-sdk-python

# Review staged changes
git status

# Commit the changes
git commit -m "chore: prepare for v1.0.0 release

- Add README.md to root directory
- Add CHANGELOG.md with v1.0.0 release notes
- Update setup.py with proper type hints
"

# Push to SDKImprovement branch
git push origin SDKImprovement
```

### Step 2: Merge to Main Branch

You have two options:

**Option A: Create a Pull Request (Recommended)**
```bash
# Push your branch if not already pushed
git push origin SDKImprovement

# Then go to GitHub and create a PR:
# https://github.com/Noveum/noveum-sdk-python/compare/main...SDKImprovement
```

**Option B: Direct Merge (if you have permissions)**
```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Merge SDKImprovement branch
git merge SDKImprovement

# Push to main
git push origin main
```

### Step 3: Create and Push Release Tag

Once your changes are on the `main` branch:

```bash
# Make sure you're on main and up to date
git checkout main
git pull origin main

# Create an annotated tag for v1.0.0
git tag -a v1.0.0 -m "Release v1.0.0 - Initial release

Features:
- Complete API coverage for 37+ v1 endpoints
- High-level and low-level client interfaces
- Full async/await and synchronous support
- Comprehensive type hints and IDE support
- Complete test suite with 213 unit tests
- Production-ready with security scanning
"

# Push the tag to GitHub
git push origin v1.0.0
```

### Step 4: Monitor Release Workflow

After pushing the tag, the release workflow will automatically trigger:

1. **Watch the workflow**: https://github.com/Noveum/noveum-sdk-python/actions
2. **Workflow steps**:
   - ✅ Run unit tests
   - ✅ Run integration tests (requires `NOVEUM_API_KEY` secret)
   - ✅ Build package (wheel and source distribution)
   - ✅ Validate package with twine
   - ✅ Publish to PyPI (via Trusted Publishing)
   - ✅ Create GitHub Release with artifacts

3. **Expected duration**: 5-10 minutes

### Step 5: Verify Release

After the workflow completes:

1. **Check PyPI**: https://pypi.org/project/noveum-sdk-python/
2. **Test installation**:
   ```bash
   # In a new virtual environment
   pip install noveum-sdk-python
   python -c "from noveum_api_client import NoveumClient; print('Success!')"
   ```
3. **Check GitHub Release**: https://github.com/Noveum/noveum-sdk-python/releases/tag/v1.0.0

## Troubleshooting

### Issue: Trusted Publishing Not Configured
**Error**: "Trusted publishing exchange failure"

**Solution**: 
1. Go to https://pypi.org/manage/account/publishing/
2. Add the pending publisher configuration (see above)
3. Wait a few minutes and retry

### Issue: Integration Tests Failing
**Error**: Integration tests fail during release

**Solution**:
1. Ensure `NOVEUM_API_KEY` is set in GitHub Secrets
2. Go to: https://github.com/Noveum/noveum-sdk-python/settings/secrets/actions
3. Add secret: `NOVEUM_API_KEY` with your valid API key

### Issue: Tag Already Exists
**Error**: "tag 'v1.0.0' already exists"

**Solution**:
```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin :refs/tags/v1.0.0

# Create new tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### Issue: Build Fails
**Error**: Package build fails

**Solution**:
1. Test build locally:
   ```bash
   pip install build twine
   python -m build
   twine check dist/*
   ```
2. Fix any issues
3. Commit and push
4. Delete and recreate the tag

## Post-Release Tasks

After a successful release:

1. ✅ Update version in `pyproject.toml` to next development version (e.g., `1.0.1-dev`)
2. ✅ Add "Unreleased" section to CHANGELOG.md
3. ✅ Announce the release (if applicable)
4. ✅ Update documentation if needed

## Quick Reference Commands

```bash
# Current directory
cd /Users/mramanindia/work/noveum-sdk-python

# Commit changes
git commit -m "chore: prepare for v1.0.0 release"
git push origin SDKImprovement

# Merge to main (after PR approval or directly)
git checkout main
git pull origin main
git merge SDKImprovement
git push origin main

# Create and push tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Watch release
open https://github.com/Noveum/noveum-sdk-python/actions

# Verify on PyPI
open https://pypi.org/project/noveum-sdk-python/
```

## Release Workflow Details

The release workflow (`.github/workflows/release.yml`) performs:

1. **Test Job**:
   - Runs on Ubuntu with Python 3.11
   - Executes unit tests
   - Executes integration tests (requires API key)

2. **Build Job**:
   - Builds wheel and source distribution
   - Validates with twine
   - Uploads artifacts

3. **Publish Job**:
   - Uses PyPI Trusted Publishing (OIDC)
   - No tokens required in repository
   - Publishes to https://pypi.org/p/noveum-sdk-python

4. **GitHub Release Job**:
   - Creates GitHub release
   - Attaches build artifacts
   - Generates release notes automatically
   - Marks as prerelease if tag contains 'alpha', 'beta', or 'rc'

## Security Notes

- ✅ No PyPI tokens stored in repository
- ✅ Uses OpenID Connect (OIDC) for authentication
- ✅ Short-lived credentials
- ✅ Audit trail on PyPI
- ✅ Only runs on tag pushes to `main` branch

## Need Help?

- **GitHub Actions**: https://github.com/Noveum/noveum-sdk-python/actions
- **PyPI Project**: https://pypi.org/project/noveum-sdk-python/
- **Trusted Publishing Docs**: https://docs.pypi.org/trusted-publishers/

---

**Last Updated**: January 9, 2026  
**Current Version**: 1.0.0  
**Ready for Release**: ✅ Yes

