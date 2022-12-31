# Hipshot
Hipshot is a python tool for taking full page screenshots of websites either single-handedly, or with multiple URL's.

I created this to speed up my design audit process. 

## Setting up Selenium
[make this better]
* Download Selenium Drivers for Chrome here: https://chromedriver.storage.googleapis.com/index.html
* Place driver in "seleniumdrivers" folder
* Place in PATH environment variable 

## Later
* Use Selenium to detect if pop-up has shown up on screen
* Error handing for: 
  * If website title has "." or "/" in title which won't work 
    * Or I could use Regex to strip away any non folder/filename friendly characters   