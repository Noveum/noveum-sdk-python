# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-09

### Added
- Initial release of Noveum SDK Python client
- Complete API coverage for all 37+ v1 endpoints
- High-level `NoveumClient` wrapper for common operations
- Low-level `Client` for direct API access
- Full async/await and synchronous support
- Comprehensive type hints and IDE support
- Complete test suite (unit + integration tests)
- API key authentication
- Support for:
  - Datasets management
  - Traces and telemetry
  - Scorers and scorer results
  - Projects and webhooks
  - ETL jobs
  - AI chats
  - Credentials management
  - Authentication flows
  - API keys management
  - And more...

### Documentation
- Comprehensive README with examples
- Architecture documentation
- Usage guide
- API reference
- Contributing guidelines
- Engineer verification guide

### Testing
- 213 unit tests with mocked responses
- Comprehensive integration test suite
- CI/CD pipeline with GitHub Actions
- Code coverage tracking with Codecov

### Security
- Security scanning with Bandit
- Dependency vulnerability checking with Safety
- HTTPS-only API communication
- Secure API key handling

[1.0.0]: https://github.com/Noveum/noveum-sdk-python/releases/tag/v1.0.0
