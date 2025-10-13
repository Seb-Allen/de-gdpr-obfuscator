from src.extract import extract
from src.transform import transform
from src.load import load


def main(json_input):
    extraction_response = extract(json_input)
    
    if extraction_response['status'] == 'Failure':
        print(extraction_response)
        exit()
    
    file_to_obfuscate = extraction_response['file_object']
    transform_response = transform(json_input, file_to_obfuscate)

    if transform_response['status'] == 'Failure':
        print(transform_response)
        exit()

    clean_file = transform_response['clean_file']

    load_response = load(clean_file)

    if load_response['status'] == 'Failure':
        print(load_response)
        exit()

    obfuscated_file_stream = load_response['buffer']

    return obfuscated_file_stream