
import boto3

def upload_logs(bucket_name, file_path):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, file_path.split("/")[-1])
    print(f"Uploaded {file_path} to {bucket_name}")
            