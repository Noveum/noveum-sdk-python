# Changelog

All notable changes to the Noveum SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-12-16

### Added

- **Initial Release**: Complete Python SDK for Noveum.ai AI/ML evaluation platform
- **Core Features**:
  - Real-time evaluation API for scoring agent/model outputs
  - Dataset management with automatic pagination
  - Scorer configuration and management
  - Trace submission and retrieval
  - Full async/await support with `AsyncNoveumClient`
  
- **Authentication**:
  - API key-based authentication
  - Environment variable support (`NOVEUM_API_KEY`)
  - Custom base URL configuration
  
- **Error Handling**:
  - 15 granular exception types
  - Automatic retry logic with exponential backoff
  - Rate limit handling with retry-after support
  
- **Data Models**:
  - Pydantic v2 models for all API objects
  - Full type hints throughout
  - Automatic validation and serialization
  
- **Helper Utilities**:
  - `EvalAggregator` for analyzing evaluation results
  - `ScorerConfigBuilder` for fluent scorer configuration
  - `DatasetItemBuilder` for fluent dataset item creation
  - Batch operations and filtering functions
  - Performance monitoring utilities
  
- **Testing**:
  - 80 comprehensive tests (72 unit + 8 integration)
  - 100% coverage of core functionality
  - Real API integration tests
  - Mock-based unit tests
  
- **Documentation**:
  - Comprehensive README with examples
  - Architecture guide
  - Contributing guidelines
  - Inline docstrings for all modules
  - Type hints for IDE support

### Resources

- **Traces**: Submit and retrieve traces
- **Datasets**: Load and manage evaluation datasets
- **Scorers**: List available scorers and view results
- **Evals**: Primary resource for real-time evaluation (CI/CD focused)

### Dependencies

- `httpx` (^0.25.0): Modern HTTP client with async support
- `pydantic` (^2.0.0): Data validation and serialization
- `pydantic-settings` (^2.0.0): Configuration management
- `python-dotenv` (^1.0.0): Environment variable loading

### Development Dependencies

- `pytest` (^7.0.0): Testing framework
- `pytest-asyncio` (^0.21.0): Async test support
- `black` (^23.0.0): Code formatter
- `ruff` (^0.1.0): Linter
- `mypy` (^1.0.0): Type checker

---

## Planned Features

### v0.2.0 (Q1 2026)

- Webhook support for async evaluation notifications
- Batch streaming for large-scale evaluations
- Advanced filtering and querying for datasets
- Custom scorer creation and management
- Performance optimizations and caching

### v0.3.0 (Q2 2026)

- Multi-language support (TypeScript SDK)
- GraphQL API support
- Advanced analytics and reporting
- Integration with popular ML frameworks

### v1.0.0 (Q3 2026)

- Stable API guarantee
- Production-grade performance and reliability
- Comprehensive documentation and examples
- Community contributions and ecosystem

---

## Migration Guides

### From Pre-Release Versions

This is the initial release. No migration needed.

---

## Support

For issues, feature requests, or questions:

- **GitHub Issues**: [noveum-sdk-python/issues](https://github.com/Noveum/noveum-sdk-python/issues)
- **Email**: support@noveum.ai
- **Documentation**: [docs.noveum.ai](https://docs.noveum.ai)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
