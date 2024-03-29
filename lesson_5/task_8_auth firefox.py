from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

#зайти на site
driver.get("http://the-internet.herokuapp.com/login")
# #три раза кликните на кнопку .
input_username=driver.find_element(By.CSS_SELECTOR,'input#username')
input_username.send_keys("tomsmith")
input_password=driver.find_element(By.CSS_SELECTOR,'input#password')
input_password.send_keys("SuperSecretPassword!")
button=driver.find_element(By.CSS_SELECTOR,'button.radius')
button.click()
driver.quit()