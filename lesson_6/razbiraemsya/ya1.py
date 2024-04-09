from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def sdelay_scrinschot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)
    browser.save_screenshot('./ya_'+browser.name+'.png')
    browser.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


sdelay_scrinschot(chrome)
sdelay_scrinschot(edge)
sdelay_scrinschot(ff)