from tkinter import *
import threading
from classes.webdriver import Webdriver
import sqlite3

class Run:
    def __init__(self, root, count, url, actions):
        self.root = root
        self.count = count
        print(url)
        
        # Create a Label for displaying the count
        self.count_label = Label(self.root, text="Count: 0", font=("Helvetica", 12))
        self.count_label.pack(side="top", pady=5)
        
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
                    # self.driver.onhold(5)
                elif do_function == "send_key":
                    if isinstance(action['value'],dict):
                        table = action['value']['table']
                        column = action['value']['column']
                        row = i + 1
                        value = getData(table,column,row)
                        self.driver.assigenValue(action["type"], action["path"], value,time=action['delay'])
                    else:
                        # self.driver.onhold(4)
                        self.driver.assigenValue(action["type"], action["path"], action["value"],time=action['delay'])
                        # self.driver.onhold(4)
                else:
                    print("Unknown function:", do_function)
            self.driver.onhold(5)
            self.driver.onDelete()


# db.py


def getData(table, column, row, db_path="database/user_details.db"):
    conn = sqlite3.connect(db_path)  # Create a new connection for the current thread
    cursor = conn.cursor()
    try:
        result = cursor.execute(f'''SELECT {column} FROM {table} WHERE rowid = {row}''').fetchone()
        return result[0] if result else None
    finally:
        conn.close()  # Ensure the connection is closed after use
