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
  driver.get('https://www.saucedemo.com/')
  #Auth
  driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys('standard_user')
  driver.find_element(By.CSS_SELECTOR,'#password').send_keys('secret_sauce')
  driver.find_element(By.CSS_SELECTOR,'#login-button').click()
  driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack').click()
  driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt').click()
  driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-onesie').click()
  driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link').click()
  driver.find_element(By.CSS_SELECTOR,'#checkout').click()
  driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('test')
  driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('testov')
  driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('672030')
  driver.find_element(By.CSS_SELECTOR,'#continue').click()
  waiter = WebDriverWait(driver, 60, 0.1)
  waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.summary_total_label'),'58.29')
  )
