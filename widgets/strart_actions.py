import customtkinter as ctk
import threading
import sqlite3
import time
import queue  # For thread-safe communication
from models.webdriver import Webdriver


class StartAction:
    def __init__(self, master):
        self.runner = ctk.CTkToplevel(master)
        self.runner.title("Running...")
        self.runner.geometry('500x400')  # Set window size to 500x400
        self.runner.transient(master)
        self.runner.grab_set()
        self.runner.resizable(False, False)
        self.range = master.count_var.get()

        # Variables
        self.start_time = time.time()
        self.time_var = ctk.StringVar(value="00:00:00")
        self.est_time_var = ctk.StringVar(value="Estimating....")
        self.status_var = ctk.StringVar(value="Starting...")
        self.count_var = ctk.StringVar(value="Counting : .....")
        self.update_est = False
        self.stop_thread = False  # Thread termination flag

        # Queue for thread-safe communication
        self.update_queue = queue.Queue()

        # Configure the grid layout of the window for centering
        self.runner.grid_rowconfigure(0, weight=1)
        self.runner.grid_rowconfigure(2, weight=1)
        self.runner.grid_columnconfigure(0, weight=1)

        # count lable
        self.count_label = ctk.CTkLabel(self.runner,textvariable=self.count_var)
        self.count_label.grid(row=0,column=0, sticky="nsew")

        # Frame to hold all widgets, centered in the window
        self.frame = ctk.CTkFrame(self.runner)
        self.frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Status Label
        self.status_label = ctk.CTkLabel(self.frame, textvariable=self.status_var, font=("Arial", 14))
        self.status_label.grid(row=0, column=0, pady=5)

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self.frame, mode="indeterminate", width=400)
        self.progress_bar.grid(row=1, column=0, pady=10)
        self.progress_bar.start()

        # Time Frame
        self.time_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.time_frame.grid(row=2, column=0, pady=5)
        self.time_label = ctk.CTkLabel(self.time_frame, text="Time:", font=("Arial", 12))
        self.time_label.grid(row=0, column=0, padx=5)
        self.time_value = ctk.CTkLabel(self.time_frame, textvariable=self.time_var, font=("Arial", 12))
        self.time_value.grid(row=0, column=1, padx=5)

        # Estimated Time Frame
        self.est_time_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.est_time_frame.grid(row=3, column=0, pady=5)
        self.est_label = ctk.CTkLabel(self.est_time_frame, text="Est. Time:", font=("Arial", 12))
        self.est_label.grid(row=0, column=0, padx=5)
        self.est_value = ctk.CTkLabel(self.est_time_frame, textvariable=self.est_time_var, font=("Arial", 12))
        self.est_value.grid(row=0, column=1, padx=5)

        # Cancel Button
        self.pause_button = ctk.CTkButton(self.frame, text="Cancel", command=self.cancel_action)
        self.pause_button.grid(row=4, column=0, pady=15)

        # Start the action in a separate thread
        self.start_action(master)

        # Start periodic queue processing
        self.runner.after(100, self.process_queue)
        self.update_timer()
        self.update_est_time()

    def start_action(self, master):
        thread = threading.Thread(target=self.loop, args=(master,))
        thread.daemon = True
        thread.start()

    def loop(self, master):
        """Background task loop."""
        try:
            for i in range(self.range):
            # Simulate interaction with Webdriver
                self.status_var.set("connecting")
                self.count_var.set(f"Count : {i+1}")
                self.cal_est_time(i)
                self.driver = Webdriver(master.url_var.get())
                for action in master.actions:
                    self.status_var.set(action["title"])
                    do_function = action["function"]
                    if do_function == "click":
                        self.driver.on_click(action["type"], action["path"])
                    elif do_function == "send_key":
                        if isinstance(action['value'],dict):
                            table = action['value']['table']
                            column = action['value']['column']
                            row = i + 1
                            value = getData(table,column,row)
                            self.driver.assigenValue(action["type"], action["path"], value,time=action['delay'])
                        else:
                            self.driver.assigenValue(action["type"], action["path"], action["value"],time=action['delay'])
                    else:
                        print("Unknown function:", do_function)
                self.driver.onhold(5)
                self.driver.onDelete()
        finally:
            self.update_queue.put(lambda: self.status_var.set("Completed"))
            self.update_queue.put(self.progress_bar.stop)

    def process_queue(self):
        """Process updates from the queue."""
        try:
            while True:
                update_func = self.update_queue.get_nowait()
                update_func()  # Execute the function on the main thread
        except queue.Empty:
            pass
        self.runner.after(100, self.process_queue)  # Check the queue again after 100ms

    def cancel_action(self):
        """Stop the thread."""
        self.stop_thread = True

    def update_timer(self):
        """Update the elapsed time display."""
        elapsed_time = int(time.time() - self.start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")
        self.runner.after(1000, self.update_timer)

    def update_est_time(self):
        if self.update_est:
            elapsed_time = self.est_elapsed_time - 1  # Decrease by 1 second to reflect countdown or update
            print(elapsed_time)
            # Format elapsed time into hours, minutes, and seconds
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Update the estimated time variable
            self.est_time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")

            # Call this method again after 1 second to keep the timer updated
            self.runner.after(1000, self.update_est_time)

    def cal_est_time(self, index):
        if index == 0:
            self.before_time = time.time()
        else:
            self.est_elapsed_time = int(time.time() - self.before_time) * (self.range - index)
            self.before_time = time.time()
            hours, remainder = divmod(self.est_elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.est_time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")


def getData(table, column, row, db_path="database/user_details.db"):
    conn = sqlite3.connect(db_path)  # Create a new connection for the current thread
    cursor = conn.cursor()
    try:
        result = cursor.execute(f'''SELECT {column} FROM {table} WHERE rowid = {row}''').fetchone()
        return result[0] if result else None
    finally:
        conn.close()  # Ensure the connection is closed after use

# # Example usage
# if __name__ == "__main__":
#     class MainApp(ctk.CTk):
#         def __init__(self):
#             super().__init__()
#             self.count_var = ctk.IntVar(value=5)
#             self.title("Main Window")
#             self.geometry("400x300")
#             self.start_button = ctk.CTkButton(self, text="Start", command=self.open_action_window)
#             self.start_button.pack(pady=50)

#         def open_action_window(self):
#             StartAction(self)

#     app = MainApp()
#     app.mainloop()
