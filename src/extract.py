import boto3
import json
from urllib.parse import urlparse

def lambda_handler(event, context):
    s3_bucket, s3_key = file_location(event)
    client = boto3.client("s3")
    file_to_obfuscate = csv_extraction(client, s3_bucket, s3_key)
    return file_to_obfuscate

def file_location(json_input):
    json_input_object = json.loads(json_input)
    
    s3_url = json_input_object['file_to_obfuscate']
    parsed_url = urlparse(s3_url, allow_fragments=False)
    
    s3_bucket = parsed_url.netloc
    s3_key = parsed_url.path.lstrip('/')

    return s3_bucket, s3_key

def csv_extraction(s3_client, s3_bucket, s3_key):    
    file_to_obfuscate = s3_client.get_object(
        Bucket=s3_bucket,
        Key=s3_key)
    return file_to_obfuscate

# if __name__ == "__main__":
#     main(json_input={})