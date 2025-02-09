PYTEST = poetry run pytest
COVERAGE = --cov=src --cov-report=term --cov-report=html:coverage_report
LAMBDA_ZIP = src/numberLambda.zip
LAMBDA_SOURCE = index.py

# Default target
all: test zip

# Run unit tests with coverage
test:
	@echo "Running unit tests with coverage..."
	$(PYTEST) $(COVERAGE)
	@echo "Tests completed. Coverage report generated in the 'coverage_report' directory."

# Clean up any temporary files or outputs
clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__ .pytest_cache coverage_report .coverage $(LAMBDA_ZIP)
	@echo "Cleanup complete."

# Zip the Lambda function code
zip:
	@echo "Zipping Lambda function code..."
	@zip $(LAMBDA_ZIP) $(LAMBDA_SOURCE)
	@echo "Lambda function code zipped into $(LAMBDA_ZIP)."

# Phony targets (targets that are not actual files)
.PHONY: all test zip clean