PYTEST = poetry run pytest
COVERAGE = --cov=src --cov-report=term --cov-report=html:coverage_report
LAMBDA_ZIP = numberLambda.zip
LAMBDA_SOURCE = src/index.py
S3_BUCKET = your-s3-bucket-name  # Replace with your S3 bucket name
S3_PREFIX = coverage-reports     # Replace with your desired S3 prefix (folder)

# Default target
all: test zip upload-coverage

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

# Upload the coverage report to S3
upload-coverage:
	@echo "Uploading coverage report to S3..."
	@aws s3 cp --recursive coverage_report/ s3://$(S3_BUCKET)/$(S3_PREFIX)/$(shell date +%Y-%m-%d_%H-%M-%S)/
	@echo "Coverage report uploaded to S3."

# Phony targets (targets that are not actual files)
.PHONY: all test zip upload-coverage clean