from src.extract import extract
from src.transform import transform
from src.load import load


def main(json_input):
    response = extract(json_input)
    
    if response['status'] == 'Failure':
        print(response)
        exit()
    else:
        clean_file = transform(json_input, response['file_object'])


        
    

    
    # clean_file = transform(json_input, file_to_obfuscate)
    # load(clean_file)
    # return response['file_object'].read().decode('utf8')