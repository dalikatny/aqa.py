from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

#зайти на site
driver.get("http://the-internet.herokuapp.com/entry_ad")
# #три раза кликните на кнопку .
modal_button=driver.find_element(By.CSS_SELECTOR,'div.modal-footer')
modal_button.click()
modal_button.click()
modal_button.click()
driver.quit()