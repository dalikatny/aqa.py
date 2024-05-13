from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
class MainPage:
    def __init__(self,driver):
        self._driver=driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    
    def form_filling(self):
        self._driver.find_element(By.CSS_SELECTOR,'[name="first-name"]').send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR,'[name="last-name"]').send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR,'[name="address"]').send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR,'[name="e-mail"]').send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR,'[name="phone"]').send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR,'[name="city"]').send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR,'[name="country"]').send_keys('Россия')
        self._driver.find_element(By.CSS_SELECTOR,'[name="job-position"]').send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR,'[name="company"]').send_keys('SkyPro')
    
    def click_submit(self):
     self._driver.find_element(By.CSS_SELECTOR,'button').click()

    def exist(self,arr, needl):
        for x in arr:
            if x == needl:
                return True
    
        return False


    def classesOfElement(self,el: WebElement):
        c = el.get_attribute("class")
 
        return c.split(" ")
    
    
    def asserting_color(self):
        
        input = self._driver.find_elements(By.CSS_SELECTOR,'.alert')

        for x in input:
                classes = self.classesOfElement(x)

                if (x.get_attribute("id") == "zip-code"):
                    assert self.exist(classes, "alert-danger")  == True
                    continue

                assert self.exist(classes, "alert-success")  == True
