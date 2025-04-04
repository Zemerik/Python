import requests
from getpass import getpass

# GitHub API example
token = getpass("Enter GitHub token: ")
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Create issue
data = {
    "title": "API Generated Issue",
    "body": "Created via Python requests"
}
response = requests.post(
    "https://api.github.com/repos/{user}/{repo}/issues",
    headers=headers,
    json=data
)
print(f"Created issue: {response.json()['html_url']}")