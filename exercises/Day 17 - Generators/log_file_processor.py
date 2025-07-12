"""
Exercise 1: Log File Processor with Generators
Create a log file processor that:
- Reads large log files line-by-line using generators
- Filters lines containing "ERROR"
- Yields formatted error messages
"""

def read_log_file(filename):
    """Generator to read a file line by line"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def filter_errors(lines):
    """Generator to filter lines containing 'ERROR'"""
    for line in lines:
        if 'ERROR' in line:
            yield line

def format_error_messages(lines):
    """Generator to format error messages"""
    for line in lines:
        yield f"[ERROR FOUND] {line}"

def process_log_file(filename):
    """Process log file and yield formatted error messages"""
    lines = read_log_file(filename)
    error_lines = filter_errors(lines)
    formatted_errors = format_error_messages(error_lines)
    return formatted_errors

def main():
    print("=== Log File Processor with Generators ===")
    # For demonstration, create a sample log file
    sample_log = "sample_log.txt"
    with open(sample_log, 'w', encoding='utf-8') as f:
        f.write("""
2024-06-01 12:00:00 INFO INIT: System started
2024-06-01 12:01:00 ERROR AUTH_FAIL: Invalid password
2024-06-01 12:02:00 WARN API_TOKEN: token expired
2024-06-01 12:03:00 DEBUG SESSION: User session started
2024-06-01 12:04:00 ERROR DB_CONN: Could not connect to DB
""")
    for msg in process_log_file(sample_log):
        print(msg)

if __name__ == "__main__":
    main() 