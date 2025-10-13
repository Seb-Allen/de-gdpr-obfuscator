from src.extract import extract
from src.transform import transform, pii_fields
import pytest
import json

class TestExtractsPiiFieldsToObfuscate:
    @pytest.mark.it("extracts PII Fields to obfuscate from JSON input")
    def test_extract_pii_fields(self):
        json_input = {
            "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        json_input = json.dumps(json_input)
        
        response = pii_fields(json_input)
        
        assert isinstance(response, list)
        assert response == ["name", "email_address"]

class TestObfuscation:
    @pytest.mark.it("tests obfuscation functionality")
    def test_obfuscation(self, csv_ingestion):
        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()
        
        response = pii_fields(json_input)
        response = extract(json_input)
        file_to_obfuscate = response['file_object']

        transform(json_input, file_to_obfuscate)