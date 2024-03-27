from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://uitestingplayground.com/classattr")
#три раза кликните на кнопку .
search_button=driver.find_element(By.CSS_SELECTOR,'btn.btn-primary')
search_button.click()
search_button.click()
search_button.click()