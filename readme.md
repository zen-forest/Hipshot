# Hipshot
Hipshot is a python tool that will take desktop and mobile screenshots of any site you need. You can do so individually or pass in a list of URLs. I needed this and built my own tool after not being too satisfied with what exists. 

## How to use 

### 1. Install selenium
```
pip install selenium
```

### 2. Check your Chrome version and download the corresponding Chrome Driver
The Chrome Driver is an exe that runs on behalf of the code written using Selenium.

You can use other browsers, but in this case we're using Google Chrome. Copy this into your URL bar to see your current version:
```
chrome://version
```
Go to this URL, find the driver that matches your Chrome release and operating system. Use ARM-64 if on an M1 Mac. 
```
https://chromedriver.storage.googleapis.com/index.html
```

## Setting up Selenium
[make this better]
* Download Selenium Drivers for Chrome here: https://chromedriver.storage.googleapis.com/index.html
* Place driver in "seleniumdrivers" folder
* Place in PATH environment variable 

## Later
* Use Selenium to detect if pop-up has shown up on screen
* Or I could use Regex to strip away any non folder/filename friendly characters 
* Error handling
* CLI(?)
* Flask server? Could create a simple API. 