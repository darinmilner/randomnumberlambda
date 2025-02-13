import boto3
from datetime import datetime, timezone

# Initialize the S3 client
s3_client = boto3.client('s3')

# Specify the bucket name and folder
bucket_name = 'your-bucket-name'
folder_name = 'outputs/'

# Define the exact target datetime (February 12th, 2025, 19:17 UTC)
target_datetime = datetime(2025, 2, 12, 19, 17, tzinfo=timezone.utc)

# Define the string to search for in the file contents
search_string = 'ModuleVersion 5.1.3'

# Initialize variables for pagination
continuation_token = None
files_with_search_string = []

# Use pagination to list all objects in the folder
while True:
    # List objects with pagination
    if continuation_token:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=folder_name,
            ContinuationToken=continuation_token
        )
    else:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=folder_name
        )

    # Filter files created at the exact target datetime
    for obj in response.get('Contents', []):
        last_modified = obj['LastModified']
        if last_modified == target_datetime:
            file_key = obj['Key']
            try:
                # Download the file
                file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
                file_content = file_obj['Body'].read().decode('utf-8')

                # Check if the file contains the search string
                if search_string in file_content:
                    files_with_search_string.append(file_key)
            except Exception as e:
                print(f"Error processing file {file_key}: {e}")

    # Check if there are more objects to retrieve
    if response.get('NextContinuationToken'):
        continuation_token = response['NextContinuationToken']
    else:
        break

# Print the files that match the criteria
if files_with_search_string:
    print(f"Files created at {target_datetime} containing '{search_string}':")
    for file in files_with_search_string:
        print(file)
else:
    print(f"No files were created at {target_datetime} in the '{folder_name}' folder containing '{search_string}'.")