import requests
from bs4 import BeautifulSoup

# Fetch webpage
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract book titles
titles = soup.select("h3 > a")
print("First 5 Book Titles:")
for title in titles[:5]:
    print(title["title"])