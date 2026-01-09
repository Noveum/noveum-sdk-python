#!/bin/bash
#
# E2E Test Runner with Beautiful Reporting
# 
# Usage:
#   ./run_test.sh datasets    # Run dataset tests
#   ./run_test.sh traces      # Run trace tests
#   ./run_test.sh all         # Run all tests
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
print_header() {
    echo -e "${BLUE}================================================================${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}================================================================${NC}"
}

# Print success
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Print error
print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Print warning
print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check environment
check_environment() {
    print_header "Checking Environment"
    
    # Check API key
    if [ -z "$NOVEUM_API_KEY" ]; then
        print_error "NOVEUM_API_KEY not set"
        echo ""
        echo "Fix: export NOVEUM_API_KEY='nv_your_key_here'"
        echo ""
        exit 1
    else
        print_success "NOVEUM_API_KEY is set"
    fi
    
    # Check optional vars
    if [ -z "$NOVEUM_PROJECT" ]; then
        print_warning "NOVEUM_PROJECT not set (using default: SDK_Test_Project)"
    else
        print_success "NOVEUM_PROJECT=$NOVEUM_PROJECT"
    fi
    
    if [ -z "$NOVEUM_ENVIRONMENT" ]; then
        print_warning "NOVEUM_ENVIRONMENT not set (using default: test)"
    else
        print_success "NOVEUM_ENVIRONMENT=$NOVEUM_ENVIRONMENT"
    fi
    
    # Check SDK installation
    if python -c "import noveum_api_client" 2>/dev/null; then
        print_success "SDK is installed"
    else
        print_error "SDK not installed"
        echo ""
        echo "Fix: pip install -e ../.."
        echo ""
        exit 1
    fi
    
    # Check pytest
    if command -v pytest &> /dev/null; then
        print_success "pytest is available"
        USE_PYTEST=1
    else
        print_warning "pytest not installed (will use standalone mode)"
        echo "   Install with: pip install pytest"
        USE_PYTEST=0
    fi
    
    echo ""
}

# Run test with pytest
run_pytest() {
    local test_file=$1
    print_header "Running: $test_file (pytest mode)"
    pytest "$test_file" -v --tb=short --color=yes
}

# Run test standalone
run_standalone() {
    local test_file=$1
    print_header "Running: $test_file (standalone mode)"
    python "$test_file"
}

# Main execution
main() {
    local test_type=${1:-all}
    
    check_environment
    
    case $test_type in
        datasets)
            if [ $USE_PYTEST -eq 1 ]; then
                run_pytest "test_datasets.py"
            else
                run_standalone "test_datasets.py"
            fi
            ;;
        traces)
            if [ $USE_PYTEST -eq 1 ]; then
                run_pytest "test_traces.py"
            else
                run_standalone "test_traces.py"
            fi
            ;;
        all)
            if [ $USE_PYTEST -eq 1 ]; then
                print_header "Running All Tests (pytest mode)"
                pytest test_datasets.py test_traces.py -v --tb=short --color=yes
            else
                run_standalone "test_datasets.py"
                echo ""
                run_standalone "test_traces.py"
            fi
            ;;
        *)
            echo "Usage: $0 {datasets|traces|all}"
            echo ""
            echo "Examples:"
            echo "  $0 datasets  # Run dataset tests"
            echo "  $0 traces    # Run trace tests"
            echo "  $0 all       # Run all tests"
            exit 1
            ;;
    esac
}

# Run main
cd "$(dirname "$0")"
main "$@"

