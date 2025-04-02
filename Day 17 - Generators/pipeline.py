def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    for line in lines:
        if not line.startswith("#"):
            yield line

def uppercase(lines):
    for line in lines:
        yield line.upper()

# Process pipeline
processed = uppercase(filter_comments(read_large_file("data.txt")))
for result in processed:
    print(result)