PYTEST = pytest
COVERAGE = --cov=src --cov-report=term --cov-report=html:coverage_report

# Default target
all: test

# Run unit tests with coverage
test:
	@echo "Running unit tests with coverage..."
	$(PYTEST) $(COVERAGE)
	@echo "Tests completed. Coverage report generated in the 'coverage_report' directory."

# Clean up any temporary files or outputs
clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__ .pytest_cache coverage_report .coverage
	@echo "Cleanup complete."

# Phony targets (targets that are not actual files)
.PHONY: all test clean