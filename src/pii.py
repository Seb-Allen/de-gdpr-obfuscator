'''
comments should explain the why, not the how or what. Code should be sufficiently readable.

MVP
- csv held in s3
- obfuscate name and email data from csv
- tool is invoked with json input specifying file and pii fields
- output will be a bytestream, compatible with boto3 s3 put_object


- json input:
{
    "file_to_obfuscate": "s3://my_ingestion_bucket/new_data/file1.csv"
    "pii_fields": ["name", "email_address"]
}

- csv looks like:
student_id,name,course,cohort,graduation_date,email_address
****
1234,'John Smith','Software','2024-03-31','j.smith@email.com'
****

- bytestream output:
student_id,name,course,cohort,graduation_date,email_address
****
1234,'***','Software','2024-03-31','***'
****

'''

def main():
    pass

if __name__ == "__main__":
    main()