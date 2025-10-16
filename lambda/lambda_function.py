from src.main import main
import json
import boto3

DESTINATION_BUCKET = "<YOUR BUCKET>"
DESTINATION_KEY = "<YOUR KEY>.csv"

def lambda_handler(event, context):
    try:
        json_input = json.dumps(event)

        obfuscated_file_stream = main(json_input)

        if obfuscated_file_stream['status'] == 'Failure':
            return obfuscated_file_stream

        s3_client = boto3.client("s3")
        s3_client.put_object(
            Body=obfuscated_file_stream.read().decode('utf8'),
            Bucket=DESTINATION_BUCKET,
            Key=DESTINATION_KEY
        )

        return {
            'status': 'Success',
            'message': f'Obfuscated file has been uploaded to s3://{DESTINATION_BUCKET}/{DESTINATION_KEY}'
        }
    
    except Exception as e:
        return {
        'status': 'Failure',
        'error': str(e)
    }