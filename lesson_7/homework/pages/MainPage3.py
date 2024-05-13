from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def auth (self):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_clothes (self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_the_cart(self):
        self._driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link').click()

    def click_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR,'#checkout').click()

    def filling_mail_data(self):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('test')
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('testov')
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('672030')
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def total_sum(self):
        waiter = WebDriverWait(self._driver, 60, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.summary_total_label'), '58.29')
        )