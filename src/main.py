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
    
    print(transform_response['clean_file'])

    load(transform_response('clean_file'))
        
    

    
    # clean_file = transform(json_input, file_to_obfuscate)
    # load(clean_file)
    # return response['file_object'].read().decode('utf8')