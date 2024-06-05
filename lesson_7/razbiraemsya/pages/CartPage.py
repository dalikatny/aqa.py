from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CartPage:
    def __init__(self, driver):
        self._driver=driver 

    def check_cart_counter(self):
        a=self._driver.find_element(By.CSS_SELECTOR, '#ui-id-4')
        txt=a.find_element(By.CSS_SELECTOR,'b').text
        return int(txt)