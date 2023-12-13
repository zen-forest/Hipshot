# Hipshot
Hipshot is a python tool that will take desktop and mobile screenshots of any site you need. Like most products and services I encounter in my life, I'm left disatified and wanting to build my own version. 

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

## Version 2: CLI
- [x] Prototype with single URL's
- [x] Accept inputs via command and add to list
- [x] Check URL validity
- [ ] Figure out way to have multiple URLs inputted via CLI, with option to add another vs. run script 
- [ ] Refactor code as learning exercise - probably want an init to spin up chromedriver once 

## Version 3: Create Flask app 
- [ ] As a test, make sure I can deploy Selenium properly - main bottleneck 
- [ ] Front-end UI for accepting URLs (probably want limit)
- [ ] Refactor code to accept URL's with a rate limit
- [ ] Host output somewhere and add to downloads 
- [ ] Dark mode, clean lines, etc.
