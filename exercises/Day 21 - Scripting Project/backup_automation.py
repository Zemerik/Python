"""
Exercise 2: Backup Automation System
Build a backup automation system that:
- Compresses project files daily
- Uploads to cloud storage
- Maintains 7-day rotation
(Simulate all steps with print statements.)
"""

import os
from datetime import datetime, timedelta

class BackupAutomation:
    """Simulate backup automation: compress, upload, rotate"""
    
    def __init__(self, project_dir="./project", backup_dir="./backups"):
        self.project_dir = project_dir
        self.backup_dir = backup_dir
        self.cloud_storage = "CloudDrive"
    
    def compress_files(self):
        today = datetime.now().strftime("%Y%m%d")
        archive_name = f"backup_{today}.zip"
        print(f"Compressing {self.project_dir} into {archive_name}...")
        return archive_name
    
    def upload_to_cloud(self, archive_name):
        print(f"Uploading {archive_name} to {self.cloud_storage}...")
    
    def rotate_backups(self):
        print("Checking for old backups to delete (keep last 7 days)...")
        # Simulate finding old backups
        backups = [f"backup_{(datetime.now() - timedelta(days=i)).strftime('%Y%m%d')}.zip" for i in range(10)]
        old_backups = backups[7:]
        for old in old_backups:
            print(f"Deleting old backup: {old}")
        print("Rotation complete. Only last 7 backups kept.")
    
    def run_backup(self):
        archive = self.compress_files()
        self.upload_to_cloud(archive)
        self.rotate_backups()

def main():
    print("=== Backup Automation System ===")
    backup = BackupAutomation()
    backup.run_backup()

if __name__ == "__main__":
    main() 