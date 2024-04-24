from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


def exist(arr, needl):
  for x in arr:
    if x == needl:
      return True
    
  return False


def classesOfElement(el: WebElement):
 c = el.get_attribute("class")
 
 return c.split(" ")

def test_selenium():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.maximize_window()
  driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
  driver.find_element(By.CSS_SELECTOR,'[name="first-name"]').send_keys('Иван')
  driver.find_element(By.CSS_SELECTOR,'[name="last-name"]').send_keys('Петров')
  driver.find_element(By.CSS_SELECTOR,'[name="address"]').send_keys('Ленина, 55-3')
  driver.find_element(By.CSS_SELECTOR,'[name="e-mail"]').send_keys('test@skypro.com')
  driver.find_element(By.CSS_SELECTOR,'[name="phone"]').send_keys('+7985899998787')
  driver.find_element(By.CSS_SELECTOR,'[name="city"]').send_keys('Москва')
  driver.find_element(By.CSS_SELECTOR,'[name="country"]').send_keys('Россия')
  driver.find_element(By.CSS_SELECTOR,'[name="job-position"]').send_keys('QA')
  driver.find_element(By.CSS_SELECTOR,'[name="company"]').send_keys('SkyPro')
  driver.find_element(By.CSS_SELECTOR,'button').click()


  input = driver.find_elements(By.CSS_SELECTOR,'.alert')

  for x in input:
      classes = classesOfElement(x)

      if (x.get_attribute("id") == "zip-code"):
        assert exist(classes, "alert-danger")  == True
        continue

      assert exist(classes, "alert-success")  == True
