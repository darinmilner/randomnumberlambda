import boto3
import csv
from datetime import datetime, timezone
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

# Specify the bucket name and folder
bucket_name = 'your-bucket-name'
folder_name = 'outputs/'

# Define the target date (February 12th, 2025)
target_date = datetime(2025, 2, 12, tzinfo=timezone.utc).date()

# Initialize variables for pagination
continuation_token = None
files_created_on_target_date = []

# Local directory to download files
download_dir = 's3files'
os.makedirs(download_dir, exist_ok=True)

# CSV file to export the data
csv_file = 'files-created-on-2025-02-12.csv'

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
            file_key = obj['Key']
            files_created_on_target_date.append({
                'File Name': file_key,
                'Created Date': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S UTC')
            })

            # Download the file
            local_file_path = os.path.join(download_dir, os.path.basename(file_key))
            s3_client.download_file(bucket_name, file_key, local_file_path)
            print(f"Downloaded: {file_key} to {local_file_path}")

    # Check if there are more objects to retrieve
    if response.get('NextContinuationToken'):
        continuation_token = response['NextContinuationToken']
    else:
        break

# Export the data to a CSV file
if files_created_on_target_date:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['File Name', 'Created Date'])
        writer.writeheader()
        writer.writerows(files_created_on_target_date)
    print(f"Exported data to {csv_file}")
else:
    print(f"No files were created on {target_date} in the '{folder_name}' folder.")

# Print the files created on the target date
if files_created_on_target_date:
    print(f"Files created on {target_date}:")
    for file in files_created_on_target_date:
        print(f"File Name: {file['File Name']}, Created Date: {file['Created Date']}")
else:
    print(f"No files were created on {target_date} in the '{folder_name}' folder.")