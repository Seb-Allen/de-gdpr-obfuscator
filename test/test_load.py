from src.extract import extract
from src.transform import transform
from src.load import load
import pytest

class TestBufferData:
    @pytest.mark.it("Test original data remains unchanged")
    def test_original_data(self, s3_client, csv_ingestion):
        
        original_csv = s3_client.get_object(
            Bucket="test_bucket",
            Key="test_csv.csv"
        )
        
        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()
        
        extraction_response = extract(json_input)
        file_to_obfuscate = extraction_response['file_object']
        transform_response = transform(json_input, file_to_obfuscate)
        clean_file = transform_response['clean_file']
        obfuscated_file_stream = load(clean_file)

        original_csv_after_ETL = s3_client.get_object(
            Bucket="test_bucket",
            Key="test_csv.csv"
        )

        assert original_csv['Body'].read() == original_csv_after_ETL['Body'].read()

    @pytest.mark.it("test that buffer is a bytes object")
    def test_bytesIO(self, csv_ingestion):
        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()
        
        extraction_response = extract(json_input)
        file_to_obfuscate = extraction_response['file_object']
        transform_response = transform(json_input, file_to_obfuscate)
        clean_file = transform_response['clean_file']
        obfuscated_file_stream = load(clean_file)
        
        assert isinstance(obfuscated_file_stream.read(), bytes)