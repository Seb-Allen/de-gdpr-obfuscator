import boto3
import json
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def extract(json_input):
    s3_bucket, s3_key = file_location(json_input)
    client = boto3.client("s3")
    file_object = file_extraction(client, s3_bucket, s3_key)
    return file_object

def file_location(json_input):
    json_input_object = json.loads(json_input)
    
    s3_url = json_input_object['file_to_obfuscate']
    parsed_url = urlparse(s3_url, allow_fragments=False)
    
    s3_bucket = parsed_url.netloc
    s3_key = parsed_url.path.lstrip('/')

    return s3_bucket, s3_key

def file_extraction(s3_client, s3_bucket, s3_key):
    try:
        file_object = s3_client.get_object(
            Bucket=s3_bucket,
            Key=s3_key)
        logger.info("File successfully retrieved")
        return {
        'status': 'Success',
        'file_object': file_object['Body']
    }
    
    except Exception as e:
        logger.error(e)
        return {
            'status': 'Failure',
            'error': e,
            'advice': 'Check the s3 url supplied for file_to_obfuscate'
        }