import boto3


def main():
    client = s3_client()
    csv_ingestion(client)
    some_function()


def some_function():
    pass

def s3_client():
    return boto3.client("s3")

def csv_ingestion(s3_client):
    with open('./test/test_data/test_csv.csv', 'r') as file:
        s3_client.put_object(
            Bucket="nc-de-test",
            Key="test_csv.csv",
            Body=file.read()            
        )
    
    response = s3_client.get_object(
        Bucket="nc-de-test",
        Key="test_csv.csv")
    
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
    # print(response)
    # print(response['Body'].read().decode('utf-8'))







if __name__ == "__main__":
    main()