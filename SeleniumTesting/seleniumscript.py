from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# Setting up test driver and target domain
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-devshm-using")
options.add_argument("--window-size=1920,1080")
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
firefox_binary = "/usr/bin/firefox"
driver = webdriver.Firefox(
    options=options, capabilities=cap, firefox_binary=firefox_binary)
driver.get("34.126.115.32:5000")
time.sleep(3)
assert driver.title == 'SaveMe'
