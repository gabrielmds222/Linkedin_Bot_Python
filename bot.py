from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://www.linkedin.com/feed/")


input('')