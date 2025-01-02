from tkinter import *
import threading
from classes.webdriver import Webdriver

class Run:
    def __init__(self, root, count, url, actions):
        self.root = root
        self.count = count
        print(url)
        
        # Create a Label for displaying the count
        self.count_label = Label(self.root, text="Count: 0", font=("Helvetica", 12))
        self.count_label.pack(side="top", pady=20)
        
        # Start the loop in a separate thread
        thread = threading.Thread(target=self.loop, args=(actions, url))
        thread.daemon = True  # Ensure thread exits when the main program ends
        thread.start()
    
    def updateUI(self, count):
        # Update the Label text on the main thread
        self.root.after(0, lambda: self.count_label.config(text=f"Count: {count + 1}"))
    
    def loop(self, actions, url):
        self.updateUI(0)
        for i in range(self.count):
            print(f"Running iteration: {i + 1}")
            self.updateUI(i)
            
            # Simulate interaction with Webdriver
            self.driver = Webdriver(url)
            for action in actions:
                do_function = action["function"]
                if do_function == "click":
                    self.driver.on_click(action["type"], action["path"])
                    self.driver.onhold(5)
                elif do_function == "send_key":
                    self.driver.onhold(4)
                    self.driver.assigenValue(action["type"], action["path"], action["value"])
                    self.driver.onhold(4)
                else:
                    print("Unknown function:", do_function)
            self.driver.onDelete()
