def transform(json_input, file_to_obfuscate):
    columns_to_delete = pii_fields(json_input)
    obfuscate(columns_to_delete, file_to_obfuscate)

def pii_fields():
    pass

def obfuscate(colunns_to_delete, file_to_obfuscate):
    pass