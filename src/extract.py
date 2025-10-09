import boto3
import json

def main(json_input):
    s3_bucket, s3_key = file_location(json_input)
    client = s3_client()
    file_to_obfuscate = csv_extraction(client, s3_bucket, s3_key)
    return file_to_obfuscate

def file_location(json_input):
    s3_bucket = "test_bucket"
    s3_key = "test_csv.csv"
    return s3_bucket, s3_key

def s3_client():
    return boto3.client("s3")

def csv_extraction(s3_client, s3_bucket, s3_key):    
    file_to_obfuscate = s3_client.get_object(
        Bucket=s3_bucket,
        Key=s3_key)
    return file_to_obfuscate

if __name__ == "__main__":
    main()