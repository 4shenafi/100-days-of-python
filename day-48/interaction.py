from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\src\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

time.sleep(2)  # Wait for 2 seconds before interacting

search = driver.find_element(By.NAME, "search")
search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)

input("Press Enter to continue...")
