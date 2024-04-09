from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://ya.ru')
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.set_window_size(100,60)
