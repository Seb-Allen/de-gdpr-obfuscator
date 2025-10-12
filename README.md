# GDPR Obfuscator
This simple tool reads csv files stored in s3 and removes predefined Personally Identifiable Information (PII).

This tool can be uploaded to Lambda, or run from the Command Line Interface (CLI).

```bash
pyton -i src/main.py
```
```python-repl
with open('src/json_input.json', 'r') as file:
    json_input=file.read()

file = extract(json_input)
print(file)
```