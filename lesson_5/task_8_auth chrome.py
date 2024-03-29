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
input_username=driver.find_element(By.CSS_SELECTOR,'input#username')
input_username.send_keys("tomsmith")
input_password=driver.find_element(By.CSS_SELECTOR,'input#password')
input_password.send_keys("SuperSecretPassword!")
button=driver.find_element(By.CSS_SELECTOR,'button.radius')
button.click()