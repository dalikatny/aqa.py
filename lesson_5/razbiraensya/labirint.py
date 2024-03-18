#зайти на лабиринт
#найти книг по слову Python
#собрать все карточки товаров
#вывести в консоль название, автор, цена
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на лабиринт
driver.get("https://www.labirint.ru/")

#найти книг по слову Python
search_input=driver.find_element(By.CSS_SELECTOR,'#search-field')
search_input.send_keys('Python',Keys.ENTER)

#собрать все карточки товаров

book_locator='div.product-card'
books=driver.find_elements(By.CSS_SELECTOR,book_locator)
print(len(books))

#вывести в консоль название, автор, цена
for book in books:
    title=''
    try:
        title=book.find_element(By.CSS_SELECTOR,'a.product-card__name').text
    except:
        title='Название не указано' 
    price=''
    try:
        price=book.find_element(By.CSS_SELECTOR,'div.product-card__price-current').text
    except:
        price='Цена не указана'
    author=''
    try:
        author=book.find_element(By.CSS_SELECTOR,'div.product-card__author').text
    except:
        author='Автор не указан'    
    #print('"',title,'",','"',author,'",','"',price,'"',)
    print(title + "\t" + author + "\t" + price )
    
sleep(5)