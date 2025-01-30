import requests
from bs4 import BeautifulSoup

# Fetch the HTML content from the website
yc_response = requests.get("https://news.ycombinator.com/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(yc_response.text, "html.parser")

# Find all the article links with the class "storylink"
articles = soup.find_all(name="a", class_="storylink")

# Print the text of each article link
for article in articles:
    print(article.getText())