import requests
from requests.exceptions import HTTPError, Timeout

try:
    response = requests.get(
        "https://api.github.com/user",
        timeout=3
    )
    response.raise_for_status()
except HTTPError as err:
    print(f"HTTP error: {err}")
except Timeout:
    print("Request timed out")
except Exception as err:
    print(f"Other error: {err}")
else:
    print("Request succeeded:", response.status_code)