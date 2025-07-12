"""
Exercise 2: File Processor Logging
Implement logging in a file processor:
- Track file operations with different log levels
- Capture exceptions with tracebacks
- Rotate logs when they reach 1MB
(Use logging module and RotatingFileHandler.)
"""

import logging
from logging.handlers import RotatingFileHandler
import os

class FileProcessor:
    def __init__(self, log_file='file_processor.log'):
        self.logger = logging.getLogger('FileProcessor')
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=3)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def process_file(self, filename):
        self.logger.info(f'Starting processing: {filename}')
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f'{filename} not found')
            with open(filename) as f:
                data = f.read()
            self.logger.debug(f'Read {len(data)} bytes from {filename}')
        except Exception as e:
            self.logger.error(f'Error processing {filename}', exc_info=True)
        else:
            self.logger.info(f'Finished processing: {filename}')

def main():
    print('=== File Processor Logging ===')
    fp = FileProcessor()
    fp.process_file('example.txt')
    fp.process_file('missing.txt')

if __name__ == '__main__':
    main() 