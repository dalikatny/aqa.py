from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://the-internet.herokuapp.com/login")
# #три раза кликните на кнопку .
search_input=driver.find_element(By.CSS_SELECTOR,'input#username')
search_input.send_keys("tomsmith")
search_input=driver.find_element(By.CSS_SELECTOR,'input#password')
search_input.send_keys("SuperSecretPassword!")
search_input=driver.find_element(By.CSS_SELECTOR,'button.radius')
search_input.click()
sleep(2)