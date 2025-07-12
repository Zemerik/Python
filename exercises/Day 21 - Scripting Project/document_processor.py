"""
Exercise 1: Document Processor Script
Create a script that:
- Converts all .txt files in directory to PDF
- Adds timestamp to filenames
- Moves processed files to archive folder
(Simulate PDF conversion and file moves with print statements.)
"""

import os
from datetime import datetime

class DocumentProcessor:
    """Simulate document processing: txt to PDF, timestamp, archive"""
    
    def __init__(self, directory="./docs", archive="./archive"):
        self.directory = directory
        self.archive = archive
    
    def process_documents(self):
        print(f"Scanning directory: {self.directory}")
        # Simulate finding .txt files
        txt_files = [f for f in ["report.txt", "notes.txt", "summary.txt"] if f.endswith('.txt')]
        print(f"Found .txt files: {txt_files}")
        for fname in txt_files:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_name = fname.replace('.txt', f'_{timestamp}.pdf')
            print(f"Converting {fname} to {pdf_name} (PDF)...")
            print(f"Moving {pdf_name} to archive folder: {self.archive}")
        print("All documents processed and archived.")

def main():
    print("=== Document Processor Script ===")
    processor = DocumentProcessor()
    processor.process_documents()

if __name__ == "__main__":
    main() 