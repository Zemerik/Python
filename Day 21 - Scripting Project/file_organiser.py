import os
import shutil
from pathlib import Path

def organize_files(directory="Downloads"):
    file_types = {
        "Images": [".jpg", ".png", ".webp"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Code": [".py", ".js", ".html"]
    }

    for file in Path(directory).iterdir():
        if file.is_file():
            dest_dir = "Other"
            for category, extensions in file_types.items():
                if file.suffix.lower() in extensions:
                    dest_dir = category
                    break
            
            (Path(directory)/dest_dir).mkdir(exist_ok=True)
            shutil.move(str(file), str(Path(directory)/dest_dir/file.name))

if __name__ == "__main__":
    organize_files()