from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://the-internet.herokuapp.com/inputs")
# #три раза кликните на кнопку .
search_input=driver.find_element(By.CSS_SELECTOR,'input')
search_input.send_keys("1000")
search_input.clear()
search_input.send_keys("999")
