"""
Exercise 2: Log Parser
Build a log parser that:
- Extracts timestamps from logs
- Captures error codes/messages
- Redacts sensitive information
"""

import re

class LogParser:
    """Log parser using regular expressions"""
    
    TIMESTAMP_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\b")
    ERROR_PATTERN = re.compile(r"\b(ERROR|WARN|INFO|DEBUG)\b.*?\b([A-Z0-9_]+)\b: (.+)")
    SENSITIVE_PATTERN = re.compile(r"(password|token|secret)=[^\s]+", re.IGNORECASE)
    
    def extract_timestamps(self, log):
        """Extract all timestamps from log text"""
        return self.TIMESTAMP_PATTERN.findall(log)
    
    def extract_errors(self, log):
        """Extract error codes and messages from log text"""
        return self.ERROR_PATTERN.findall(log)
    
    def redact_sensitive(self, log):
        """Redact sensitive information from log text"""
        return self.SENSITIVE_PATTERN.sub(r"\1=***REDACTED***", log)
    
    def parse_log(self, log):
        print("Timestamps:", self.extract_timestamps(log))
        print("Errors:", self.extract_errors(log))
        print("Redacted log:")
        print(self.redact_sensitive(log))

def main():
    print("=== Log Parser ===")
    parser = LogParser()
    sample_log = """
2024-06-01 12:00:00 INFO INIT: System started
2024-06-01 12:01:00 ERROR AUTH_FAIL: Invalid password=password123
2024-06-01 12:02:00 WARN API_TOKEN: token=abcdef123456 expired
2024-06-01 12:03:00 DEBUG SESSION: User session started
2024-06-01 12:04:00 ERROR DB_CONN: Could not connect to DB secret=supersecret
"""
    parser.parse_log(sample_log)

if __name__ == "__main__":
    main() 