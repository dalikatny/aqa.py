from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

#зайти на site
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Пять раз кликните на кнопку Add Element.
search_button=driver.find_element(By.CSS_SELECTOR,'button[onclick="addElement()"')
search_button.click()
search_button.click()
search_button.click()
search_button.click()
search_button.click()
#Соберите со страницы список кнопок Delete.
delete_locator='button.added-manually'
delete=driver.find_elements(By.CSS_SELECTOR,delete_locator)
#Выведите на экран размер списка.
print(len(delete))
driver.quit()