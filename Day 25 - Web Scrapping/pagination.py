import requests
from bs4 import BeautifulSoup

base_url = "https://example.com/news?page="

for page in range(1, 6):
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.select(".article")
    print(f"Page {page} Articles:", len(articles))
    
    # Add scraping logic here