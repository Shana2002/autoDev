from tkinter import *
from classes.webdriver import Webdriver
class Run:
    def __init__(self,root ,count,url,actions):
        self.root = root
        self.count = count
        self.driver = Webdriver(url)

        
    def updateUI(self,count):
        Label(text=f"count {count+1}").pack(side="top", pady=20)
    
    def loop(self,actions):
        for i in range(0,self.count):
            self.updateUI(i)
            for action in actions:
                do_function = action["function"]
                if do_function == "click":
                    self.driver.on_click(action["type"],action["path"])
                    self.driver.onhold(5)
                elif do_function == "send_key":
                    self.driver.onhold(4)
                    self.driver.assigenValue(action["type"],action["path"],action["value"])
                    self.driver.onhold(4)
                else :
                    print("error")
            