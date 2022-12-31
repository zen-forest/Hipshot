import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

s = Service('/user/local/bin/chromerdriver')
driver = webdriver.Chrome()

driver.get("http://www.python.org")

driver.implicitly_wait(1)

driver.save_screenshot("Screeshot.png")

driver.quit()