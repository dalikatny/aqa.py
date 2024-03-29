from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
#зайти на site
driver.get("http://uitestingplayground.com/classattr")
#три раза кликните на кнопку .
blue_button=driver.find_element(By.CSS_SELECTOR,'btn.btn-primary')
blue_button.click()
blue_button.click()
blue_button.click()
driver.quit()