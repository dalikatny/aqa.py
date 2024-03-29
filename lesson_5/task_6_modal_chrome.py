from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://the-internet.herokuapp.com/entry_ad")
# #три раза кликните на кнопку .
modal_button=driver.find_element(By.CSS_SELECTOR,'div.modal-footer')
modal_button.click()
modal_button.click()
modal_button.click()