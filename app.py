import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service




# Get the current working directory
cwd = os.getcwd()

urls = [ "https://www.harborfreight.com",
         "https://www.bose.com/en_us/index.html",
         "https://www.onepeloton.com/",
         "https://www.everlane.com/products/mens-organic-slim-fit-jean-faded-sky?collection=mens-bestsellersv2",
         "https://www.whirlpool.com/",
         "https://www.homedepot.com/",
         "https://store.google.com/us/category/connected_home?hl=en-US&GoogleNest&utm_source=nest_redirect&utm_medium=google_oo&utm_campaign=homepage&pli=1",
         "https://www.beatsbydre.com/earbuds/studio-buds?sku=MJ503",
         "https://www.outdoorvoices.com"
]

def take_screenshots(url):
  # Set up chrome driver
  s = Service('/user/local/bin/chromerdriver')
  driver = webdriver.Chrome()
  
  # Point the driver towards the URL
  driver.get(url)
  
  # Get the page 
  page_title = driver.title
  
  # Create a new folder
  os.makedirs(page_title)
  
  # Create valid screenshots paths for folders and files
  screenshot_path = os.path.join(cwd, f"{page_title}", f" {page_title}desktop.png")
  screenshot_path_mobile = os.path.join(cwd, f"{page_title}", f" {page_title}mobile.png")
  
  # Take desktop screenshot
  driver.save_screenshot(screenshot_path)
  
  # Resize and take mobile screenshot
  driver.set_window_size(375, 2080)
  driver.save_screenshot(screenshot_path_mobile)

  # Print status message
  print(f"Screenshots created for {page_title} in {page_title} folder")

  driver.implicitly_wait(1)
  driver.quit()
  
# Run a loop on the list of URL's above
def automate(urls):
  for url in urls:
    take_screenshots(url)

automate(urls)

