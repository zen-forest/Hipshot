import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service



def single_URL_screenshot(url):
  # Hook up selenium to driver
  s = Service('/user/local/bin/chromerdriver')
  driver = webdriver.Chrome()

  # Point driver towards desired URL and take screenshot
  driver.get("http://www.python.org")
  driver.implicitly_wait(1)
  driver.save_screenshot("Screeshot.png")
  driver.quit()