# Changelog

All notable changes to the Noveum SDK Python client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-21

### Added
- Enhanced integration test coverage for complete API workflows
- Improved security with removal of potentially sensitive API endpoints
- Comprehensive test suite for API keys and telemetry
- Updated documentation for testing procedures

### Changed
- Streamlined CI/CD pipeline by removing redundant workflow files
- Improved test organization and structure
- Enhanced error handling and logging in integration tests
- Better test fixtures and helper utilities

### Fixed
- Test reliability improvements across all integration tests
- Documentation references and internal links
- Test cleanup and resource management

## [1.0.3] - 2026-01-12

### Added
- Comprehensive testing documentation in `TESTING.md`
- Enhanced README badges for CI, Release, and Python version
- Improved test coverage reporting
- Additional integration test documentation

### Changed
- Updated README.md with enhanced badge styles
- Improved documentation structure and references
- Enhanced error handling examples

### Fixed
- Documentation references now properly linked
- Test configuration improvements

## [1.0.2] - 2026-01-10

### Added
- Complete integration test suite with 60+ tests
- Unit test suite with 45+ tests covering all SDK functionality
- Test helper scripts for convenient test execution
- Comprehensive test fixtures and mocks

### Changed
- Improved test organization and structure
- Enhanced test documentation in subdirectories
- Updated pytest configuration for better test execution

### Fixed
- Test reliability improvements
- Fixed intermittent test failures
- Improved test cleanup and resource management

## [1.0.1] - 2026-01-05

### Added
- High-level `NoveumClient` wrapper for simplified API access
- Convenience methods: `list_datasets()`, `get_dataset_items()`, `get_results()`
- Context manager support for automatic connection cleanup
- Comprehensive error handling examples
- Extended documentation and usage guides

### Changed
- Improved API response formatting consistency
- Enhanced type hints and IDE support
- Better error messages and debugging information

### Fixed
- SSL certificate verification handling
- Timeout configuration issues
- Response parsing edge cases

## [1.0.0] - 2026-01-01

### Added
- Initial production release of Noveum SDK Python client
- Complete API coverage with 180+ endpoints
- Full support for all API categories:
  - Administration
  - AI Chats
  - API Keys
  - Authentication
  - Credentials
  - Datasets
  - ETL Jobs
  - Health/Status
  - Organizations
  - Projects
  - Scorer Results
  - Scorers
  - Telemetry
  - Telemetry Plugins
  - Traces
  - Webhooks
- Both synchronous and asynchronous API support
- 700+ Pydantic data models with full type hints
- Complete IDE support with autocomplete and docstrings
- Comprehensive documentation:
  - README.md with quick start and examples
  - ARCHITECTURE.md for technical details
  - USAGE_GUIDE.md for detailed usage instructions
  - CONTRIBUTING.md for contribution guidelines
  - RELEASE_GUIDE.md for release process
  - VERIFICATION_CHECKLIST.md for QA
- Production-ready test suite:
  - Integration tests with live API
  - Unit tests with mocked responses
  - Test fixtures and helpers
- CI/CD integration with GitHub Actions
- Code coverage reporting with codecov.io
- PyPI publishing with Trusted Publishing
- Python 3.10, 3.11, 3.12 support
- Apache 2.0 license

### Security
- API key authentication support
- HTTPS-only communication
- Secure credential management
- SSL certificate verification

## [0.9.0] - 2025-12-20

### Added
- Beta release for testing and feedback
- Core API client functionality
- Generated API endpoints from OpenAPI schema
- Basic documentation and examples
- Initial test coverage

### Changed
- Refactored client architecture
- Improved error handling
- Enhanced type definitions

### Fixed
- Various bug fixes and stability improvements
- Documentation corrections

## [0.8.0] - 2025-12-15

### Added
- Alpha release for internal testing
- Auto-generated API client from OpenAPI specification
- Basic authentication support
- Core data models
- Initial documentation

---

## Version History

- **1.0.3** (Current) - Enhanced documentation and testing
- **1.0.2** - Complete test suite
- **1.0.1** - High-level wrapper and improved UX
- **1.0.0** - Initial production release
- **0.9.0** - Beta release
- **0.8.0** - Alpha release

## Links

- [PyPI Package](https://pypi.org/project/noveum-sdk-python/)
- [GitHub Repository](https://github.com/Noveum/noveum-sdk-python)
- [Documentation](https://noveum.ai/docs)
- [API Reference](https://noveum.ai/docs/api)

## Release Notes Guidelines

### Version Format

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible new features
- **PATCH**: Backwards-compatible bug fixes

### Change Categories

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be-removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing changes.

## Support

For questions or issues:
- **GitHub Issues**: https://github.com/Noveum/noveum-sdk-python/issues
- **Email**: support@noveum.ai
- **Documentation**: https://noveum.ai/docs
