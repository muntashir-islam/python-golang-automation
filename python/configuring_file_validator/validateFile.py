#Reads the file.
#Stores the valid key-value pairs in a dictionary.
#Ignores lines that are empty or start with # (comments).
#Raises an error (or prints a warning) if a line is missing the = separator.
def validate_file(file_path):
    config = {}
    with open(file_path, 'r') as file:
        content = file.readlines()
        for line_num, line in enumerate(content, 1):
            line = line.strip()
            if line.startswith('#'):
                continue
            if '=' not in line:
                print(f"Warning: Line {line_num} in config is invalid (missing '='): '{line}'")
                continue
            try:
                key, value = line.split('=', 1)
                config[key] = value.strip()
            except ValueError:
                print(f"Warning: Skipping malformed line {line_num}: '{line}'")
    return config


parsed_config = validate_file('example.txt')
print("\n--- Parsed Config ---")
print(parsed_config)
