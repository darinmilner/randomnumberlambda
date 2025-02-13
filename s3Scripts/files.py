import boto3
from datetime import datetime

# Initialize the S3 client
s3_client = boto3.client('s3')

# Specify the bucket name and folder
bucket_name = 'your-bucket-name'
folder_name = 'outputs/'

# Define the date you're interested in
target_date = datetime(2025, 2, 12).date()

# Initialize variables for pagination
continuation_token = None
files_created_on_target_date = []

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

    # Filter files created on the target date
    for obj in response.get('Contents', []):
        last_modified = obj['LastModified'].date()
        if last_modified == target_date:
            files_created_on_target_date.append(obj['Key'])

    # Check if there are more objects to retrieve
    if response.get('NextContinuationToken'):
        continuation_token = response['NextContinuationToken']
    else:
        break

# Print the files created on the target date
if files_created_on_target_date:
    print(f"Files created on {target_date}:")
    for file in files_created_on_target_date:
        print(file)
else:
    print(f"No files were created on {target_date} in the '{folder_name}' folder.")