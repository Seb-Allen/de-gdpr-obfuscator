import polars as pl
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def transform(json_input, file_to_obfuscate):

    fields_to_obfuscate = pii_fields(json_input)
    response = obfuscate(fields_to_obfuscate, file_to_obfuscate)
    return response



def pii_fields(json_input):
    try:
        json_input = json.loads(json_input)

        fields_to_obfuscate = json_input['pii_fields']
        
        return fields_to_obfuscate
    
    except Exception as e:
        return f'Could not extract PII Fields: {e}'



def obfuscate(fields_to_obfuscate, file_to_obfuscate):
    try:

        df = pl.read_csv(file_to_obfuscate)
        
        for field in fields_to_obfuscate:
            df = df.lazy().with_columns(pl.lit("***").alias(field))
        
        clean_file = df.collect()
        
        logger.info("File successfully retrieved")
        
        return {
            'status': 'Success',
            'clean_file': clean_file
        }
    
    except Exception as e:
        return {
            'status': 'Failure',
            'error': e
        }