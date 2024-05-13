import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from pages_2.MainPage import MainPage

def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver);
    main_page.set_timer(45)
    main_page.click_the_button()
    main_page.wait_for_visible_result()
    time.sleep(5)
