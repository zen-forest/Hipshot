import os
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



# Get the current working directory
cwd = os.getcwd()

urls = [ "https://www.everlane.com/products/mens-organic-slim-fit-jean-faded-sky?collection=mens-bestsellersv2",
         "https://www.specialized.com/us/en/turbo-levo-comp-carbon/p/216806?color=349650-216806",
         "https://www.bose.com/en_us/products/headphones/noise_cancelling_headphones/quietcomfort-headphones-45.html#v=qc45_black",
         "https://www.onepeloton.com/tread",
         "https://www.beatsbydre.com/earbuds/studio-buds?sku=MJ503",
         "https://www.standstilltea.com/product/oolong",
         "https://www.harborfreight.com/vertical-milling-machine-40939.html",
         "https://www.woodcraft.com/products/shark-sd110-cnc-machine-next-wave?via=573621bd69702d0676000002%2C5763ffe769702d6582000e3a",
         "https://www.samsung.com/us/home-appliances/refrigerators/bespoke/bespoke-3-door-french-door-refrigerator--30-cu--ft---with-autofill-water-pitcher-in-stainless-steel-rf30bb6200qlaa/",
         "https://www.samsung.com/us/home-appliances/cooktops-and-hoods/electric-cooktops/30--built-in-electric-cooktop-with-rapid-boil-nz30k6330rs-aa/",
         "https://www.whirlpool.com/kitchen/cooking/cooktops/electric/p.24-inch-compact-electric-ceramic-glass-cooktop.wce55us4hb.html?",
         "https://www.samsung.com/us/home-appliances/cooktops-and-hoods/electric-cooktops/30--built-in-electric-cooktop-with-rapid-boil-nz30k6330rs-aa/"
         "https://www.electrolux.com/en/p/kitchen/refrigerators/french-door-refrigerators/ERFC2393AS",  
         "https://www.lg.com/us/washer-dryer-combos/lg-LUWM101HWA-washer-dryer-combo-lgsignature",
]

# def take_screenshots(url):
#   # Set up chrome driver
#   s = Service('/user/local/bin/chromerdriver')
#   driver = webdriver.Chrome()
  
# # set up chrome options
#   chrome_options = Options()
#   chrome_options.add_argument("--headless")

#   # Point the driver towards the URL
#   driver.get(url)
  
#   # Get the page 
#   page_title = driver.title
#   folder_name = "OutputFolder"

#   # Create a new output folder
#   os.makedirs(folder_name)

#   # Create a new folder
#   os.makedirs(page_title)
  
#   # Size for desktop
#   driver.set_window_size(1100, 9080)

#   # Create valid screenshots paths for folders and files
#   screenshot_path = os.path.join(cwd, f"/{folder_name}/{page_title}", f" {page_title}desktop.png")
#   screenshot_path_mobile = os.path.join(cwd, f"/{folder_name}/{page_title}", f" {page_title}mobile.png")
  
#   # Take desktop screenshot
#   driver.save_screenshot(screenshot_path)
  
#   # Resize and take mobile screenshot
#   driver.set_window_size(375, 4080)
#   driver.save_screenshot(screenshot_path_mobile)

#   # Print status message
#   print(f"Screenshots created for {page_title} in {page_title} folder")

#   driver.implicitly_wait(1)
#   driver.quit()
  
# # # Run a loop on the list of URL's above
# # def automate(urls):
# #   for url in urls:
# #     take_screenshots(url)





class Test:
  def __init__(self):
    s = Service('/user/local/bin/chromerdriver')
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    

    folder_name = "OutputFolder"
    os.makedirs(folder_name)
  
  
  def take_screenshots(self, driver, urls):
    urls = urls

    for url in urls: 

      driver.get(url)
      page_title = driver.title
      driver.set_window_size(1100, 9080)

      # Create valid screenshots paths for folders and files
      screenshot_path = os.path.join(cwd, f"/{folder_name}/{page_title}", f" {page_title}desktop.png")
      screenshot_path_mobile = os.path.join(cwd, f"/{folder_name}/{page_title}", f" {page_title}mobile.png")
      
      # Take desktop screenshot
      driver.save_screenshot(screenshot_path)
      
      # Resize and take mobile screenshot
      driver.set_window_size(375, 4080)
      driver.save_screenshot(screenshot_path_mobile)

      # Print status message
      print(f"Screenshots created for {page_title} in {page_title} folder")

      driver.implicitly_wait(1)
      driver.quit()

a = Test()
a.take_screenshots(urls)