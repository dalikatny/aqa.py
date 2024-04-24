from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_selenium():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.maximize_window()
  driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
  driver.find_element(By.CSS_SELECTOR,'#delay').clear()
  driver.find_element(By.CSS_SELECTOR,'#delay').send_keys('45')
  
  driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()#7
  
  driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()#+
  
  driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()#8
  
  driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()#=
  

  waiter = WebDriverWait(driver, 60, 0.1)
  waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'),'15')
  )
  