from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
my_cookie= {
    'name':'cookie_policy',
    'value':'1'
}
browser.get('https://labirint.ru')
browser.add_cookie(my_cookie)
browser.refresh()
sleep(10)
browser.quit()