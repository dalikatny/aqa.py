from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://uitestingplayground.com/dynamicid")
#три раза кликните на кнопку .
button=driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
button.click()
button.click()
button.click()