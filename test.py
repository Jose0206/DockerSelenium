from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Remote(
    'http://localhost:4444/wd/hub',
    desired_capabilities=webdriver.DesiredCapabilities.CHROME
)

driver.get("http://google.com")
driver.save_screenshot("test01.png")
time.sleep(5)
all_cookies = driver.get_cookies()
print(all_cookies)
