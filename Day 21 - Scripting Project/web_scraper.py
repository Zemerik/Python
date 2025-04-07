import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    with open("quotes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Author", "Quote", "Tags"])
        
        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text() for tag in quote.select(".tag")]
            writer.writerow([author, text, ", ".join(tags)])

if __name__ == "__main__":
    scrape_quotes()