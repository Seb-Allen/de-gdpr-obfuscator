import pytest
from moto import mock_aws
import boto3
import os
import json


@pytest.fixture(autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.fixture(scope="function")
def s3_client():
    with mock_aws():
        yield boto3.client("s3")

@pytest.fixture(scope="function")
def test_bucket(s3_client):
    s3_client.create_bucket(
        Bucket="test_bucket",
        CreateBucketConfiguration={
            "LocationConstraint": "eu-west-2",
            "Location": {"Type": "AvailabilityZone", "Name": "string"}
        }
    )

@pytest.fixture(scope="function")
def csv_ingestion(s3_client, test_bucket):
    with open('./test/test_data/test_csv.csv', 'r') as file:
        s3_client.put_object(
            Bucket="test_bucket",
            Key="test_csv.csv",
            Body=file.read()            
        )