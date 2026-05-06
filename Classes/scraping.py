from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class Scraping:
    def __init__(self, url):
        self.url = url
        self.driver = None
        self.setUp()

    # to set up the driver and open the url
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) # to wait before any imp
        self.driver.get(self.url)
        time.sleep(2)
        # return driver
        
    # to check if the site is opened correctly by checking the title of the page
    def check_site(self, side_title) :
        try :
            time.sleep(2)
            assert side_title in self.driver.title
        except Exception as e :
            print(f"the error is {e}")
    
    # to get an element by its class name and return it
    def get_element(self, class_name):
        driver = self.driver
        try :
            element = driver.find_element(By.CLASS_NAME, class_name)
        except Exception as e :
            print(f"the error is {e}")
        return element
    
    # to send keys to the search bar and submit the search
    def send_keys_to_search_bar(self, search_bar, keys):
        try :
            search_bar.clear()
            search_bar.send_keys(keys)
            search_bar.send_keys(Keys.RETURN)
            time.sleep(2)
        except Exception as e :
            print(f"the error is {e}")
    
    # to click on an element and wait for 2 seconds
    def Click_element(self, element):
        try :
            element.click()
            time.sleep(2)
        except Exception as e :
            print(f"the error is {e}")
    
    # to get multiple elements by their class name and return them
    def get_elements(self, class_name):
        driver = self.driver
        try :
            elements = driver.find_elements(By.CLASS_NAME, class_name)
        except Exception as e :
            print(f"the error is {e}")
        return elements

    # to get the text of an element and return it
    def get_element_text(self, element):
        try :
            text = element.text
        except Exception as e :
            print(f"the error is {e}")
        return text

    # to get the driver and url of the object
    def get_driver(self):
        return self.driver
    # to get the url of the object
    def get_url(self):
        return self.url
    
    # to close the driver when the object is deleted
    def __del__(self):
        self.driver.quit()




# browser = Scraping("https://www.imdb.com/")
# browser.get_movie_comment()
