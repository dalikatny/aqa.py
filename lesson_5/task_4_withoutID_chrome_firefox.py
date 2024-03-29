from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

#зайти на site
driver.get("http://uitestingplayground.com/dynamicid")
#три раза кликните на кнопку .
button=driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
button.click()
button.click()
button.click()
driver.quit()