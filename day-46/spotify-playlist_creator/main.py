from bs4 import BeautifulSoup
import requests

# Get the target date from the user
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

song_elements = soup.find_all("h3", id="title-of-a-story", class_="c-title")

song_titles = [song.get_text(strip=True) for song in song_elements]

print(song_titles)