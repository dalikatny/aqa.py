from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
#зайти на site
driver.get("http://the-internet.herokuapp.com/inputs")
# #три раза кликните на кнопку .
search_input=driver.find_element(By.CSS_SELECTOR,'input')
search_input.send_keys("1000")
search_input.clear()
search_input.send_keys("999")
driver.quit()