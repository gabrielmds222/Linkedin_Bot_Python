from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

from config import login

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://www.linkedin.com/feed/")

input_email = browser.find_element(By.ID, "username")
input_email.send_keys(login["email"])

input_password = browser.find_element(By.ID, "password")
input_password.send_keys(login["password"])

btn_login = browser.find_element(By.XPATH, "//button[@type='submit']")
btn_login.click()

search = browser.find_element(By.XPATH, "//input[@placeholder='Pesquisar']")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

time.sleep(3)

job_filter = browser.find_element(By.XPATH, "//button[text()='Vagas']")
job_filter.click()

input('')