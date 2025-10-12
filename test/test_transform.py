from src.transform import pii_fields
import pytest

class TestExtractsPiiFieldsToObfuscate:
    @pytest.mark.it("extractss PII Fields to obfuscate from JSON input")
    def  test_extract_pii_fields(self):
        json_input = {
            "file_to_obfuscate": "s3://test_bucket/test_csv.csv",
            "pii_fields": [
                "name",
                "email_address"
                ]
                }
        
        response = pii_fields(json_input)
        assert response == ""