from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from lesson_7.homework.pages.MainPage3 import MainPage


def test_color_zipcode():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver);
    main_page.auth()
    main_page.add_clothes()
    main_page.go_to_the_cart()
    main_page.click_checkout()
    main_page.filling_mail_data()
    main_page.total_sum()