from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://uitestingplayground.com/classattr")
#три раза кликните на кнопку .
search_input=driver.find_element(By.CSS_SELECTOR,'button.btn.class1')
sleep(2)
search_input.click()
sleep(2)
search_input.click()
sleep(2)
search_input.click()
sleep(2)