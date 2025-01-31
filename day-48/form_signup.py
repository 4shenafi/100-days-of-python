from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\src\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Ashenafi")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Pawlos")
email = driver.find_element(By.NAME, "email")
email.send_keys("ashenafipaul21@gmail.com")
submit = driver.find_element(By.CLASS_NAME, "btn")
submit.click()


input("Press Enter to continue...")