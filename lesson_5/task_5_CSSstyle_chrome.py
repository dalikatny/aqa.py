from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://uitestingplayground.com/classattr")
#три раза кликните на кнопку .
blue_button=driver.find_element(By.CSS_SELECTOR,'btn.btn-primary')
blue_button.click()
blue_button.click()
blue_button.click()