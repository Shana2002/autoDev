import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Webdriver:
    
    def __init__(self,weblink):
        service = Service(ChromeDriverManager().install())
        self.__new_driver = webdriver.Chrome(service=service)
        self.__new_driver.get(weblink)
        
    
    def on_click(self,type,path):
        try:
            clickable = self.__new_driver.find_element(by=type,value='//*[@id="myForm"]/div[4]')
            clickable.click()
            return True
        except Exception as e:
            return False,e
        
    
    def assigenValue(self,type,path,value):

        try:
            value_assigner = self.__new_driver.find_element(by=type,value=path)
            value_assigner.send_keys(value)
            return True
        except Exception as e:
            return False,e

        
    
    def onhold(self,var_time):
        time.sleep(var_time)

    def onDelete(self):
        self.__new_driver.quit()

new_drive = Webdriver("http://localhost:5500/login.html")

new_drive.assigenValue(By.ID,'username',"hansaka")
new_drive.assigenValue(By.ID,'password',"hansaka")
new_drive.on_click("a","NPEfkd.RveJvd.snByac")
