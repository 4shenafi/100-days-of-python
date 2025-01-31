from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r"C:\src\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the cookie element to load
time.sleep(5)  # Give the page time to load (better to use WebDriverWait)

# Correctly find the cookie element by ID
cookie = driver.find_element(By.ID, "bigCookie")

# Click the cookie in an infinite loop
while True:
    cookie.click()
