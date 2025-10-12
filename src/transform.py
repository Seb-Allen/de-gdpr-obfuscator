import polars
from io import BytesIO

def transform(json_input, file_to_obfuscate):
    columns_to_delete = pii_fields(json_input)
    obfuscate(columns_to_delete, file_to_obfuscate)

def pii_fields(json_input):
    return ""

def obfuscate(colunns_to_delete, file_to_obfuscate):
    pass