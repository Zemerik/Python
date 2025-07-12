"""
Exercise 2: News Aggregator
Build a news aggregator that:
- Scrapes article headlines and summaries
- Follows "next page" links
- Avoids duplicate content
(Simulate HTML and requests if no real site.)
"""

from bs4 import BeautifulSoup

class NewsAggregator:
    """Simulate scraping news headlines/summaries across pages"""
    
    def __init__(self):
        # Simulate HTML for two pages with a next link
        self.pages = [
            '''<html><body>
                <div class="article"><h2>Headline 1</h2><p>Summary 1</p></div>
                <div class="article"><h2>Headline 2</h2><p>Summary 2</p></div>
                <a href="page2.html" class="next">Next</a>
            </body></html>''',
            '''<html><body>
                <div class="article"><h2>Headline 3</h2><p>Summary 3</p></div>
                <div class="article"><h2>Headline 2</h2><p>Summary 2</p></div>
            </body></html>'''
        ]
    
    def scrape(self):
        seen = set()
        results = []
        for page_html in self.pages:
            soup = BeautifulSoup(page_html, 'html.parser')
            for article in soup.find_all('div', class_='article'):
                headline = article.find('h2').get_text(strip=True)
                summary = article.find('p').get_text(strip=True)
                if headline not in seen:
                    results.append({'headline': headline, 'summary': summary})
                    seen.add(headline)
        print("Articles scraped:")
        for art in results:
            print(f"- {art['headline']}: {art['summary']}")
        print(f"Total unique articles: {len(results)}")

def main():
    print("=== News Aggregator ===")
    aggregator = NewsAggregator()
    aggregator.scrape()

if __name__ == "__main__":
    main() 