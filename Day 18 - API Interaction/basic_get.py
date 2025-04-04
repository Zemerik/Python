import requests

# Public API example
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# With parameters
params = {"userId": 1}
todos = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params=params
).json()
print(f"First TODO: {todos[0]['title']}")