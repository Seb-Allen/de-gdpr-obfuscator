from src import extract, transform, load


def main(json_input):
    file_to_obfuscate = extract(json_input)
    clean_file = transform(file_to_obfuscate)
    load(clean_file)

if __name__ == "__main__":
    main(json_input={})