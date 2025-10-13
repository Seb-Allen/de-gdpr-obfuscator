from src.main import main
import pytest
import polars as pl
import json

class TestMain:
    @pytest.mark.it("test that main function successfully brings ETL together")
    def test_main(self, csv_ingestion):
        with open ('./test/test_data/test_obfuscated_csv.csv', 'r') as file:
            test_obfuscated_csv = file.read()
        
        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()

        obfuscated_file_stream = main(json_input)
        
        with open('./test/test_data/test_main_output.csv', 'w') as file:
            file.write(obfuscated_file_stream.read().decode('utf8'))

        with open('./test/test_data/test_main_output.csv', 'r') as file:
            main_output = file.read()

        assert main_output == test_obfuscated_csv     

class TestErrorHandling:
    @pytest.mark.it("test extraction failure")
    def test_extraction_failure(self, csv_ingestion):
        json_input = {
            "file_to_obfuscate": "s3://INVALID_BUCKET/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        json_input = json.dumps(json_input)

        response = main(json_input)

        assert response['status'] == 'Failure'

    @pytest.mark.it("test extraction failure")
    def test_transformation_failure(self, csv_ingestion):
        json_input = {
            "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
            "pii_fields": []
                }
        
        json_input = json.dumps(json_input)

        response = main(json_input)

        assert response['status'] == 'Failure'