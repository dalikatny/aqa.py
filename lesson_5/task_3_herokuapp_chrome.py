from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на site
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Пять раз кликните на кнопку Add Element.
button=driver.find_element(By.CSS_SELECTOR,'button[onclick="addElement()"')
button.click()
button.click()
button.click()
button.click()
button.click()
#Соберите со страницы список кнопок Delete.
delete_locator='button.added-manually'
delete=driver.find_elements(By.CSS_SELECTOR,delete_locator)
#Выведите на экран размер списка.
print(len(delete))