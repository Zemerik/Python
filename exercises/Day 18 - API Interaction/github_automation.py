"""
Exercise 2: GitHub Automation Tool
Build a GitHub automation tool that:
- Creates new repository via API
- Lists user's repositories
- Implements OAuth authentication
"""

import requests
import os

class GitHubAutomation:
    """GitHub automation tool using GitHub API"""
    
    BASE_URL = "https://api.github.com"
    DEMO_MODE = True  # Set to False to use real API
    DEMO_USER = "demo-user"
    DEMO_REPOS = ["demo-repo1", "demo-repo2"]
    
    def __init__(self, token=None):
        self.token = token or os.environ.get("GITHUB_TOKEN")
    
    def get_headers(self):
        if self.DEMO_MODE or not self.token:
            return {}
        return {"Authorization": f"token {self.token}"}
    
    def list_repos(self):
        if self.DEMO_MODE or not self.token:
            print("[Demo mode] Listing mock repositories.")
            return self.DEMO_REPOS
        url = f"{self.BASE_URL}/user/repos"
        try:
            resp = requests.get(url, headers=self.get_headers(), timeout=5)
            resp.raise_for_status()
            return [repo["name"] for repo in resp.json()]
        except Exception as e:
            print(f"Error listing repositories: {e}")
            return []
    
    def create_repo(self, name):
        if self.DEMO_MODE or not self.token:
            print(f"[Demo mode] Pretending to create repo '{name}'.")
            return True
        url = f"{self.BASE_URL}/user/repos"
        data = {"name": name, "private": False}
        try:
            resp = requests.post(url, headers=self.get_headers(), json=data, timeout=5)
            resp.raise_for_status()
            print(f"Repository '{name}' created successfully.")
            return True
        except Exception as e:
            print(f"Error creating repository: {e}")
            return False
    
    def authenticate(self):
        if self.DEMO_MODE:
            print("[Demo mode] OAuth authentication simulated.")
            return True
        # In real use, implement OAuth device flow or web flow
        print("OAuth authentication would be performed here.")
        return False

def main():
    print("=== GitHub Automation Tool ===")
    tool = GitHubAutomation()
    while True:
        print("\nOptions: 1) List repos 2) Create repo 3) Authenticate 4) Exit")
        choice = input("Choose option: ").strip()
        if choice == '1':
            repos = tool.list_repos()
            print("Repositories:", repos)
        elif choice == '2':
            name = input("Enter new repository name: ").strip()
            tool.create_repo(name)
        elif choice == '3':
            tool.authenticate()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main() 