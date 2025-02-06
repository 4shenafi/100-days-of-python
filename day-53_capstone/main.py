import requests
from bs4 import BeautifulSoup

# Fetch the HTML content
url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22north%22%3A37.9019125783496%2C%22south%22%3A37.64845409651967%2C%22east%22%3A-122.1253689897461%2C%22west%22%3A-122.7412900102539%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A1376173%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A7000%7D%2C%22beds%22%3A%7B%22min%22%3A5%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%7D"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract property cards
property_cards = soup.find_all("div", class_="property-card-class-name")

# Initialize a list to store the extracted data
properties = []

# Loop through each property card and extract details
for card in property_cards:
    try:
        address = card.find("address", class_="address-class-name")
        address = address.text.strip() if address else "N/A"

        price = card.find("span", class_="price-class-name")
        price = price.text.strip() if price else "N/A"

        link = card.find("a", class_="link-class-name")
        link = link["href"] if link else "N/A"

        properties.append({
            "address": address,
            "price": price,
            "link": link
        })
    except Exception as e:
        print(f"Error extracting data: {e}")

# Print the extracted data
for property in properties:
    print(f"Address: {property['address']}")
    print(f"Price: {property['price']}")
    print(f"Link: {property['link']}")
    print("-" * 40)