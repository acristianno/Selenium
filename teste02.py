from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = "https://www.netflix.com/browse"
browser.get(url)