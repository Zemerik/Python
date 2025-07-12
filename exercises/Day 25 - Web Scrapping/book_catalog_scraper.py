"""
Exercise 1: Book Catalog Scraper
Create a book catalog scraper that:
- Extracts titles/authors from book pages
- Handles multiple category pages
- Stores results in JSON format
(Simulate HTML and requests if no real site.)
"""

from bs4 import BeautifulSoup
import json

class BookCatalogScraper:
    """Simulate scraping book titles/authors from multiple pages"""
    
    def __init__(self):
        # Simulate HTML for two category pages
        self.pages = [
            '''<html><body>
                <div class="book"><h2>Book One</h2><span class="author">Author A</span></div>
                <div class="book"><h2>Book Two</h2><span class="author">Author B</span></div>
            </body></html>''',
            '''<html><body>
                <div class="book"><h2>Book Three</h2><span class="author">Author C</span></div>
                <div class="book"><h2>Book Four</h2><span class="author">Author D</span></div>
            </body></html>'''
        ]
    
    def scrape(self):
        results = []
        for page_html in self.pages:
            soup = BeautifulSoup(page_html, 'html.parser')
            for book in soup.find_all('div', class_='book'):
                title = book.find('h2').get_text(strip=True)
                author = book.find('span', class_='author').get_text(strip=True)
                results.append({'title': title, 'author': author})
        print("Books scraped:")
        print(json.dumps(results, indent=2))
        # Save to JSON
        with open('books.json', 'w') as f:
            json.dump(results, f, indent=2)
        print("Results saved to books.json")

def main():
    print("=== Book Catalog Scraper ===")
    scraper = BookCatalogScraper()
    scraper.scrape()

if __name__ == "__main__":
    main() 