variable "lambda_name" {
  type        = string
  description = "Name of the Lambda to deploy"
  default     = "RandomNumberLambda"
}

variable "lambda_zip" {
  type        = string
  description = "Name of the Lambda zip file"
  default     = "numberLambda"
}

variable "region" {
  type        = string
  description = "AWS Region"
  default     = "us-east-1"
}
