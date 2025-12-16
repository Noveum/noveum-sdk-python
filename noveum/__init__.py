"""
Noveum Python SDK for AI/ML evaluation platform.

The Noveum SDK provides a Python interface for interacting with the Noveum API,
enabling test integration, dataset management, and real-time evaluation of AI/ML outputs.

Quick Start:
    >>> from noveum import NoveumClient
    >>> client = NoveumClient()  # Uses NOVEM_API_KEY env var
    >>> 
    >>> # Load test dataset
    >>> for item in client.datasets.items("regression-tests"):
    ...     # Run your agent/model
    ...     output = my_agent.run(item.input_text)
    ...     
    ...     # Evaluate output
    ...     result = client.evals.score(
    ...         dataset_item=item,
    ...         agent_output=output,
    ...         scorers=[ScorerConfig(scorer_id="factuality_scorer")]
    ...     )
    ...     
    ...     # Check results
    ...     print(f"Score: {result.overall_score}/10")

Authentication:
    API keys are generated on Noveum.ai and passed to the SDK:
    
    >>> client = NoveumClient(api_key="your-api-key")
    
    Or set the NOVEM_API_KEY environment variable:
    
    >>> import os
    >>> os.environ["NOVEM_API_KEY"] = "your-api-key"
    >>> client = NoveumClient()

Resources:
    - client.datasets: Load and manage datasets
    - client.evals: Evaluate outputs in real-time (primary for CI/CD)
    - client.scorers: List available scorers and view historical results
    - client.traces: Submit and retrieve traces

Async Support:
    >>> from noveum import AsyncNoveumClient
    >>> async with AsyncNoveumClient() as client:
    ...     async for item in client.datasets.items("test-set"):
    ...         result = await client.evals.score(...)
"""

__version__ = "0.1.0"
__author__ = "Noveum Team"
__license__ = "MIT"

# Core client
from .client import AsyncNoveumClient, NoveumClient

# Authentication
from .auth import APIKeyAuth, ClientConfig

# Exceptions
from .exceptions import (
    ConnectionError,
    ConnectionTimeoutError,
    InvalidAPIKeyError,
    InvalidParameterError,
    MissingParameterError,
    NoveumAPIError,
    NoveumAuthenticationError,
    NoveumConfigurationError,
    NoveumConflictError,
    NoveumError,
    NoveumInternalError,
    NoveumNetworkError,
    NoveumNotFoundError,
    NoveumRateLimitError,
    NoveumTimeoutError,
    NoveumValidationError,
    RequestTimeoutError,
)

# Models
from .models import (
    Dataset,
    DatasetItem,
    DatasetItemType,
    DatasetVersion,
    EvalRequest,
    EvalResult,
    PaginatedResponse,
    PaginationMeta,
    Scorer,
    ScorerConfig,
    ScorerMetadata,
    ScorerResult,
    Span,
    TestResult,
    Trace,
    TraceStatus,
)

# Resources
from .resources import (
    AsyncDatasetsResource,
    AsyncEvalsResource,
    AsyncScorersResource,
    AsyncTracesResource,
    DatasetsResource,
    EvalsResource,
    ScorersResource,
    TracesResource,
)

# Helpers
from .helpers import (
    EvalAggregator,
    ScorerConfigBuilder,
    DatasetItemBuilder,
    batch_results,
    create_scorer_config,
    create_scorer_configs,
    filter_by_score,
    filter_by_status,
)

# Logging
from .logging import get_logger, setup_logging, log_performance, PerformanceMonitor

__all__ = [
    # Version
    "__version__",
    # Clients
    "NoveumClient",
    "AsyncNoveumClient",
    # Auth
    "APIKeyAuth",
    "ClientConfig",
    # Exceptions
    "NoveumError",
    "NoveumAPIError",
    "NoveumAuthenticationError",
    "NoveumNetworkError",
    "InvalidAPIKeyError",
    "NoveumNotFoundError",
    "NoveumConflictError",
    "NoveumValidationError",
    "InvalidParameterError",
    "MissingParameterError",
    "NoveumRateLimitError",
    "NoveumInternalError",
    "ConnectionError",
    "ConnectionTimeoutError",
    "RequestTimeoutError",
    "NoveumConfigurationError",
    "NoveumTimeoutError",
    # Models - Common
    "PaginatedResponse",
    "PaginationMeta",
    # Models - Datasets
    "Dataset",
    "DatasetItem",
    "DatasetItemType",
    "DatasetVersion",
    # Models - Traces
    "Trace",
    "Span",
    "TraceStatus",
    # Models - Scorers
    "Scorer",
    "ScorerMetadata",
    # Models - Evals
    "EvalRequest",
    "EvalResult",
    "ScorerConfig",
    "ScorerResult",
    "TestResult",
    # Resources
    "DatasetsResource",
    "AsyncDatasetsResource",
    "TracesResource",
    "AsyncTracesResource",
    "ScorersResource",
    "AsyncScorersResource",
    "EvalsResource",
    "AsyncEvalsResource",
    # Helpers
    "EvalAggregator",
    "ScorerConfigBuilder",
    "DatasetItemBuilder",
    "batch_results",
    "create_scorer_config",
    "create_scorer_configs",
    "filter_by_score",
    "filter_by_status",
    # Logging
    "get_logger",
    "setup_logging",
    "log_performance",
    "PerformanceMonitor",
]
