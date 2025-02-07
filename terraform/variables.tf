variable "lambda_name" {
  type        = string
  description = "Name of the Lambda to deploy"
  default     = "RandomNumberLambda"
}

variable "region" {
  type        = string
  description = "AWS Region"
  default     = "us-east-1"
}
