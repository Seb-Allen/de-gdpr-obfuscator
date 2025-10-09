from src.extract import main
import pytest

class TestReadsS3Data:
    @pytest.mark.it("successfully pulls data file from S3")
    def test_reads_s3(self, csv_ingestion):
        with open('./test/test_data/json_input.json', 'r') as file:
            json_input = file.read()

        response = main(json_input)
        print(response)
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200