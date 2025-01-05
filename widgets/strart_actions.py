import customtkinter as ctk

class StartAction:
    def __init__(self, parent):
        self.runner = ctk.CTkToplevel(parent)
        self.runner.title("Running...")
        self.runner.geometry('500x400')  # Set window size to 500x400
        self.runner.transient(parent)
        self.runner.grab_set()
        self.runner.resizable(False, False)

        # Variables
        self.time_var = ctk.StringVar(value="00:00:00")
        self.est_time_var = ctk.StringVar(value="00:00:00")

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
        self.status_label = ctk.CTkLabel(self.frame, text="Click hello world data hiii", font=("Arial", 14))
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

# Example usage
# root = ctk.CTk()
# app = StartAction(root)
# root.mainloop()
