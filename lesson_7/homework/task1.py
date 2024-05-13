from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from pages_1.MainPage import MainPage


def test_color_zipcode():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver);
    main_page.form_filling()
    main_page.click_submit()
    main_page.asserting_color()
