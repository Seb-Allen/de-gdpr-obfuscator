from src.pii import some_function
import pytest

class TestReadsS3Data:
    @pytest.mark.it("successfully pulls data file from S3")
    def test_reads_s3():
        response = some_function()
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200