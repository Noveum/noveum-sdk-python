"""
Exception and skip message constants for Integration Tests.

IMPORTANT: These messages are part of the test contract.
Changing them may affect CI/CD pipelines and test reporting.
Always consider backwards compatibility when modifying these strings.
"""

# =============================================================================
# Environment/Configuration Skip Messages
# =============================================================================

SKIP_NO_API_KEY = "NOVEUM_API_KEY environment variable not set"
SKIP_GEMINI_API_KEY_NOT_SET = "GEMINI_API_KEY not set"
SKIP_NOVEUM_TRACE_NOT_AVAILABLE = "noveum_trace not available"

# =============================================================================
# Test Data File Skip Messages
# =============================================================================

# Template: {file_path}
SKIP_TEST_DATA_FILE_NOT_FOUND = "Test data file not found: {file_path}"

# =============================================================================
# API Response Failure Messages
# =============================================================================

# Template: {response_type}
FAIL_INVALID_RESPONSE_FORMAT = "Invalid response format: {response_type}"

# API call failed message components
API_CALL_FAILED_HEADER = "\n❌ API call failed\n"
API_CALL_FAILED_EXPECTED = "   Expected: {expected_codes}\n"
API_CALL_FAILED_GOT = "   Got: {status}\n"
API_CALL_FAILED_RESPONSE = "   Response: {parsed}\n"
API_CALL_FAILED_CONTENT = "   Content: {content}\n"
API_CALL_FAILED_HINT = "\n💡 Hint: {hint}\n"

# =============================================================================
# Status Code Hints (for helpful error messages)
# =============================================================================

STATUS_CODE_HINTS = {
    401: "Check your NOVEUM_API_KEY is valid",
    403: "Your API key may lack permissions for this operation",
    404: "The requested resource was not found",
    409: "Resource already exists (conflict)",
    422: "Invalid request data (validation error)",
    500: "Server error - this may be a known API issue",
}

# =============================================================================
# Trace-Related Skip Messages
# =============================================================================

# Template: {error}
SKIP_TRACE_SENDING_FAILED = "Trace sending failed: {error}"
SKIP_NO_TRACES_SENT = "No traces sent"
# Template: {error}
SKIP_FAILED_CREATE_SINGLE_TRACE = "Failed to create single trace: {error}"
SKIP_NO_SINGLE_TRACE_ID = "No single trace ID available"
# Template: {error}
SKIP_FAILED_CREATE_BATCH_TRACES = "Failed to create batch traces: {error}"
SKIP_NO_BATCH_TRACE_IDS = "No batch trace IDs available"
SKIP_NO_TRACE_ID_RETRIEVAL = "No trace ID available for retrieval test"
SKIP_NO_TRACE_ID_SPANS = "No trace ID available for spans test"

# =============================================================================
# Dataset-Related Skip Messages
# =============================================================================

SKIP_NO_DATASET_SLUG = "No dataset slug available"
SKIP_NO_DATASET_AVAILABLE = "No dataset available"
SKIP_NO_DATASET_OR_ITEMS = "No dataset slug or items available"
SKIP_NO_DATASET_OR_VERSION = "No dataset slug or version available"
SKIP_NO_DATASET_TO_DELETE = "No dataset to delete"
SKIP_NOT_ENOUGH_ITEMS_DELETION = "Not enough items to test deletion"
SKIP_NOT_ENOUGH_ITEMS_BULK_DELETE = "Not enough items for bulk delete test"

# =============================================================================
# Scorer-Related Skip Messages
# =============================================================================

SKIP_NO_SCORER_ID = "No scorer ID available"
SKIP_NO_SCORER_AVAILABLE = "No scorer available"
SKIP_NO_SCORER_TO_DELETE = "No scorer to delete"
SKIP_MISSING_SCORER_OR_ITEMS = "Missing scorer ID or item IDs"
SKIP_MISSING_REQUIRED_CONTEXT = "Missing required context"
SKIP_MISSING_REQUIRED_CONTEXT_FULL = "Missing required context (dataset, scorer, or items)"
SKIP_NO_ITEMS_BATCH_RESULTS = "No items available for batch results"

# =============================================================================
# Scorer Results Skip Messages
# =============================================================================

SKIP_MISSING_PREREQUISITES = "Missing prerequisites"
SKIP_NO_RESULTS_AVAILABLE = "No results available"
SKIP_NO_RESULT_IDS = "No result IDs available"
SKIP_NO_RESULTS_TO_DELETE = "No results to delete"

# =============================================================================
# Project-Related Skip Messages
# =============================================================================

SKIP_NO_PROJECT_ID = "No project ID available"
SKIP_MISSING_PROJECT_OR_DATASET = "Missing project ID or dataset slug"
SKIP_MISSING_PROJECT_OR_DATASET_ID = "Missing project ID or dataset ID"
# Template: {status_code}
SKIP_CREATE_PROJECT_FAILED = "Create project failed: {status_code}"

# =============================================================================
# ETL Job-Related Skip Messages
# =============================================================================

SKIP_NO_JOB_ID = "No job ID available"
SKIP_MISSING_PROJECT_OR_DATASET_ETL = "Missing prerequisites (project or dataset)"
# Template: {status_code}
SKIP_COULD_NOT_GET_OR_CREATE_PROJECT = "Could not get or create project: {status_code}"

# =============================================================================
# Audio-Related Skip Messages
# =============================================================================

SKIP_NO_AUDIO_ID = "No audio ID available from list or upload"
SKIP_NO_AUDIO_ID_TO_DELETE = "No audio ID available to delete"
SKIP_AUDIO_FILE_NOT_FOUND = "Audio file not found - may have been deleted"
SKIP_NO_AUDIO_ID_VERIFY_DELETION = "No audio ID available to verify deletion"

# =============================================================================
# Expected Failure Messages (xfail)
# =============================================================================

# Backend Known Issues - 500 Errors
XFAIL_AUDIO_DELETION_500 = "Audio deletion returned 500 (known backend issue)"
XFAIL_DATASET_DELETION_500 = "Dataset deletion returned 500 (known backend issue)"
XFAIL_REMOVE_DATASET_500 = "Remove dataset returned 500 (known backend issue)"
XFAIL_DELETE_RESULT_500 = "Delete returned 500 (known backend issue)"
XFAIL_RESULT_DELETION_500 = "Result deletion returned 500 (known backend issue)"
XFAIL_SCORER_CREATION_500 = "Create scorer returned 500 (known backend issue)"
XFAIL_ETL_JOB_CREATION_500 = "Create ETL job returned 500 (known backend issue)"
XFAIL_ETL_JOB_DELETION_500 = "ETL job deletion returned 500 (known backend issue)"
XFAIL_PROJECT_ASSOCIATE_DATASET_500 = "Associate dataset returned 500 (known backend issue)"
XFAIL_PROJECT_DELETION_500 = "Project deletion returned 500 (known backend issue)"

# Backend Known Issues - 403 ORG_CONTEXT_MISMATCH
XFAIL_API_403_ORG_CONTEXT = "API returned 403 (ORG_CONTEXT_MISMATCH)"
XFAIL_ETL_JOBS_403_ORG_CONTEXT = "ETL jobs API returned 403 (ORG_CONTEXT_MISMATCH)"
XFAIL_PROJECTS_403_ORG_CONTEXT = "Projects API returned 403 (ORG_CONTEXT_MISMATCH)"

# Trace Ingestion Delays
XFAIL_TRACE_NOT_FOUND_INGESTION_DELAY = "Trace not found - may be ingestion delay"
XFAIL_TRACE_SPANS_NOT_FOUND_DELAY = "Trace spans not found - may be ingestion delay"
XFAIL_SINGLE_TRACE_NOT_FOUND_DELAY = "Single trace not found after waiting. May be ingestion delay."
