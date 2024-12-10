
# Telemetry Logging

This script automates uploading telemetry logs to AWS S3.

## Steps to Run

1. Install AWS CLI and configure credentials.
2. Install Boto3:
   ```
   pip install boto3
   ```
3. Use the script:
   ```
   python upload_logs.py <bucket_name> <file_path>
   ```
            