from src.extract import extract, file_location
import pytest
import json

class TestExtractsFileLocation:
    @pytest.mark.it("extracts file location from json input")
    def test_extract_file_location(self):
        simple_json_input = {
            "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        simple_json_input = json.dumps(simple_json_input)
        
        s3_bucket, s3_key = file_location(simple_json_input)

        assert s3_bucket == "test_bucket"
        assert s3_key == "test_csv.csv"

        complex_json_input = {
            "file_to_obfuscate": 
                "s3://a_long_test_bucket_123/penny/for/your/thoughts/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        complex_json_input = json.dumps(complex_json_input)

        s3_bucket, s3_key = file_location(complex_json_input)

        assert s3_bucket == "a_long_test_bucket_123"
        assert s3_key == "penny/for/your/thoughts/test_csv.csv"

class TestReadsS3Data:
    @pytest.mark.it("successfully pulls data file from S3")
    def test_reads_s3(self, csv_ingestion):

        with open('./test/test_data/test_csv.csv', 'r') as file:
            data_to_obfuscate = file.read()

        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()

        response = extract(json_input)

        assert response['ResponseMetadata']['HTTPStatusCode'] == 200
        assert response['Body'].read().decode('utf8') == data_to_obfuscate

    @pytest.mark.it("returns exception when bucket cannot be found")
    def test_invalid_bucket(self, csv_ingestion):

        json_input = {
            "file_to_obfuscate": "s3://INVALID_BUCKET/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        json_input = json.dumps(json_input)

        response = extract(json_input)

        assert response == {'Check the s3 url supplied for file_to_obfuscate: '
                            'An error occurred (NoSuchBucket) when calling '
                            'the GetObject operation: The specified bucket '
                            'does not exist'}
        
    @pytest.mark.it("returns exception when file cannot be found")
    def test_invalid_file(self, csv_ingestion):

        json_input = {
            "file_to_obfuscate": "s3://test_bucket/INVALID_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        json_input = json.dumps(json_input)

        response = extract(json_input)

        assert response == {'Check the s3 url supplied for file_to_obfuscate: '
                            'An error occurred (NoSuchKey) when calling the '
                            'GetObject operation: The specified key '
                            'does not exist.'}