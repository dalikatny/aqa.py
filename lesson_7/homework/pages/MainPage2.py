from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_timer(self,x):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(x)

    def click_the_button(self):
        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()  # 7

        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()  # +

        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()  # 8

        self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()  # =

    def wait_for_visible_result(self):
        waiter = WebDriverWait(self._driver, 60, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
        )