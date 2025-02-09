provider "aws" {
  region = var.region
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "lambda-exec-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for Lambda to write logs to CloudWatch
resource "aws_iam_role_policy" "lambda_logs_policy" {
  name = "lambda-logs-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "arn:aws:logs:*:*:*"
      }
    ]
  })
}

# Lambda Function
resource "aws_lambda_function" "random_number_lambda" {
  function_name = var.lambda_name
  handler       = "index.lambda_handler"
  runtime       = "python3.11"
  role          = aws_iam_role.lambda_role.arn

  # Path to the zipped Lambda function code
  filename         = "src/${var.lambda_zip}.zip"
  source_code_hash = filebase64sha256("src/${var.lambda_zip}.zip")

  environment {
    variables = {
      # Add any environment variables here if needed
    }
  }
}

# Lambda Function URL (optional, to invoke the Lambda via HTTP)
resource "aws_lambda_function_url" "lambda_url" {
  function_name      = aws_lambda_function.random_number_lambda.function_name
  authorization_type = "NONE"
}
