from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://uitestingplayground.com/classattr")
#три раза кликните на кнопку .
search_input=driver.find_element(By.CSS_SELECTOR,'.btn.class1.btn-primary.btn-test')
sleep(2)
search_input.send_keys(Keys.ENTER)
sleep(2)
search_input.send_keys(Keys.ENTER)
sleep(2)
search_input.send_keys(Keys.ENTER)
sleep(2)