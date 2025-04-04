import requests

def get_paginated_data(url):
    page = 1
    while True:
        response = requests.get(url, params={"page": page})
        results = response.json()
        if not results:
            break
        yield from results
        page += 1

# Example usage
for repo in get_paginated_data("https://api.github.com/users/octocat/repos"):
    print(repo["name"])