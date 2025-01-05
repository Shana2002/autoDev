import customtkinter as ctk
import threading
from models.webdriver import Webdriver
import sqlite3

class StartAction:
    def __init__(self, master):
        self.runner = ctk.CTkToplevel(master)
        self.runner.title("Running...")
        self.runner.geometry('500x400')  # Set window size to 500x400
        self.runner.transient(master)
        self.runner.grab_set()
        self.runner.resizable(False, False)
        

        # Variables
        self.time_var = ctk.StringVar(value="00:00:00")
        self.est_time_var = ctk.StringVar(value="00:00:00")
        self.status_var = ctk.StringVar(value="Starting...")

        # Configure the grid layout of the window for centering
        self.runner.grid_rowconfigure(0, weight=1)  # Center vertically
        self.runner.grid_rowconfigure(2, weight=1)  # Bottom spacing
        self.runner.grid_columnconfigure(0, weight=1)  # Center horizontally

        # Frame to hold all widgets, centered in the window
        self.frame = ctk.CTkFrame(self.runner)
        self.frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Status Label (above progress bar)
        self.status_label = ctk.CTkLabel(self.frame, textvariable=self.status_var, font=("Arial", 14))
        self.status_label.grid(row=0, column=0, pady=5)

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self.frame, mode="indeterminate", width=400)
        self.progress_bar.grid(row=1, column=0, pady=10)
        self.progress_bar.start()

        # Time Frame (to align "Time:" and "00:00:00")
        self.time_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.time_frame.grid(row=2, column=0, pady=5)

        self.time_label = ctk.CTkLabel(self.time_frame, text="Time:", font=("Arial", 12))
        self.time_label.grid(row=0, column=0, padx=5)

        self.time_value = ctk.CTkLabel(self.time_frame, textvariable=self.time_var, font=("Arial", 12))
        self.time_value.grid(row=0, column=1, padx=5)

        # Estimated Time Frame (to align "Est. Time:" and "00:00:00")
        self.est_time_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.est_time_frame.grid(row=3, column=0, pady=5)

        self.est_label = ctk.CTkLabel(self.est_time_frame, text="Est. Time:", font=("Arial", 12))
        self.est_label.grid(row=0, column=0, padx=5)

        self.est_value = ctk.CTkLabel(self.est_time_frame, textvariable=self.est_time_var, font=("Arial", 12))
        self.est_value.grid(row=0, column=1, padx=5)

        # Cancel Button
        self.pause_button = ctk.CTkButton(self.frame, text="Cancel")
        self.pause_button.grid(row=4, column=0, pady=15)
        self.start_action(master)

    def start_action(self,master):
        thread = threading.Thread(target=self.loop, args=(master,))
        thread.daemon = True  # Ensure thread exits when the main program ends
        thread.start()

    def loop(self, master):
        for i in range(master.count_var.get()):
            # Simulate interaction with Webdriver
            self.status_var.set("connecting")
            self.driver = Webdriver(master.url_var.get())
            for action in master.actions:
                self.status_var.set(action["title"])
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


def getData(table, column, row, db_path="database/user_details.db"):
    conn = sqlite3.connect(db_path)  # Create a new connection for the current thread
    cursor = conn.cursor()
    try:
        result = cursor.execute(f'''SELECT {column} FROM {table} WHERE rowid = {row}''').fetchone()
        return result[0] if result else None
    finally:
        conn.close()  # Ensure the connection is closed after use