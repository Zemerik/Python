import csv
import requests
from bs4 import BeautifulSoup

url = "https://example.com/leaderboard"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract table data
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Rank", "Player", "Score"])
    
    for row in soup.select("table tr")[1:]:  # Skip header
        cols = row.find_all("td")
        writer.writerow([cols[0].text, cols[1].text, cols[2].text])