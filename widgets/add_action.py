import customtkinter
import utilities.db

class AddAction(customtkinter.CTkToplevel):
    def __init__(self, master, action):
        super().__init__(master)
        self.master = master
        self.geometry("600x500")
        self.title("Add Action")

        # Variables for input
        self.title_var = customtkinter.StringVar(value=f"Action {action+1}")
        self.action_type_var = customtkinter.StringVar(value="click")
        self.path_type_var = customtkinter.StringVar(value="xpath")
        self.path_var = customtkinter.StringVar()
        self.value_var = customtkinter.StringVar()
        self.custome_time_var = customtkinter.IntVar(value=2)
        self.radio_type = customtkinter.IntVar(value=1)
        self.table_var = customtkinter.StringVar(value=list(utilities.db.get_table().keys())[0])
        self.colum_var = customtkinter.StringVar()
        self.column_value = []
        # Result variable
        self.result = None

        # Main UI Layout
        
        # Title
        self.title_label = customtkinter.CTkLabel(self, text="Enter Title:")
        self.title_label.grid(row=0, column=0, pady=5, padx=5)
        self.title_entry = customtkinter.CTkEntry(self, textvariable=self.title_var)
        self.title_entry.grid(row=0, column=1, pady=5, padx=5)

        # Action Type
        self.action_type_label = customtkinter.CTkLabel(self, text="Select Action Type:")
        self.action_type_label.grid(row=1, column=0, pady=5, padx=5)
        self.action_type = customtkinter.CTkOptionMenu(self, variable=self.action_type_var, values=["click", "send_key",],command=self.update_fields)
        self.action_type.grid(row=1, column=1, pady=5, padx=5)

        # Path Type
        self.path_type_label = customtkinter.CTkLabel(self, text="Select Path Type:")
        self.path_type_label.grid(row=2, column=0, pady=5, padx=5)
        self.path_type = customtkinter.CTkOptionMenu(self, variable=self.path_type_var, values=["xpath", "id", "class"])
        self.path_type.grid(row=2, column=1, pady=5, padx=5)

        # Path Entry
        self.path_label = customtkinter.CTkLabel(self, text="Enter Path:")
        self.path_label.grid(row=3, column=0, pady=5, padx=5)
        self.path_entry = customtkinter.CTkEntry(self, textvariable=self.path_var)
        self.path_entry.grid(row=3, column=1, pady=5, padx=5)

        # Delay Entry
        self.delay_label = customtkinter.CTkLabel(self, text="Delay (in seconds):")
        self.delay_label.grid(row=4, column=0, pady=5, padx=5)
        self.delay_entry = customtkinter.CTkEntry(self, textvariable=self.custome_time_var)
        self.delay_entry.grid(row=4, column=1, pady=5, padx=5)

        # radio button
        self.radiobutton_value = customtkinter.CTkRadioButton(self, text="Value",
                                                    command=self.radiobutton_event, variable= self.radio_type, value=1)
        self.radiobutton_database = customtkinter.CTkRadioButton(self, text="Database",
                                                    command=self.radiobutton_event, variable= self.radio_type, value=2)

        # Value Entry
        self.value_label = customtkinter.CTkLabel(self, text="Enter Value:")
        self.value_entry = customtkinter.CTkEntry(self, textvariable=self.value_var)

        # table selector
        self.table_lable = customtkinter.CTkLabel(self, text="Select Table :")
        self.table_selector = customtkinter.CTkOptionMenu(self, variable=self.table_var, values=list(utilities.db.get_table().keys()))
        # column selector
        self.column_label = customtkinter.CTkLabel(self, text="Select Column :")
        self.column_selector = customtkinter.CTkOptionMenu(self, variable=self.colum_var, values=self.column_value)

    def create_widgets(self):
        """Create and layout UI components."""
        # Value Entry
        self.value_label = customtkinter.CTkLabel(self, text="Enter Value:")
        self.value_label.grid(row=5, column=0, pady=5, padx=5)
        self.value_entry = customtkinter.CTkEntry(self, textvariable=self.value_var)
        self.value_entry.grid(row=5, column=1, pady=5, padx=5)

        # Buttons
        button_frame = customtkinter.CTkFrame(self)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        self.ok_button = customtkinter.CTkButton(button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side="left", padx=10)

        self.cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side="left", padx=10)

    def update_fields(self,choice):
        if choice=="send_key":
            self.radiobutton_value.grid(row=5, column=0, pady=5, padx=5)
            self.radiobutton_database.grid(row=5, column=1, pady=5, padx=5)
            self.radiobutton_event()
        else:
            self.radiobutton_value.grid_forget()
            self.radiobutton_database.grid_forget()

    def radiobutton_event(self):
        if self.radio_type.get() == 1:
            self.value_label.grid(row=6, column=0, pady=5, padx=5)
            self.value_entry.grid(row=6, column=1, pady=5, padx=5)
            self.table_lable.grid_forget()
            self.table_selector.grid_forget()
            self.column_label.grid_forget()
            self.column_selector.grid_forget()
        else :
            self.table_lable.grid(row=6, column=0, pady=5, padx=5)
            self.table_selector.grid(row=6, column=1, pady=5, padx=5)
            self.column_label.grid(row=7, column=0, pady=5, padx=5)
            self.column_selector.grid(row=7, column=1, pady=5, padx=5)
            self.value_label.grid_forget()
            self.value_entry.grid_forget()

        

    def on_ok(self):
        """Collect data and close the dialog."""
        self.result = {
            "function": self.action_type_var.get(),
            "type": self.path_type_var.get(),
            "path": self.path_var.get(),
            "value": self.value_var.get(),
            "delay": self.custome_time_var.get(),
        }
        self.destroy()

    def on_cancel(self):
        """Cancel and close the dialog."""
        self.result = None
        self.destroy()

    def show(self):
        """Show the dialog and wait for user input."""
        self.grab_set()  # Make dialog modal
        self.wait_window()  # Wait until the window is closed
        return self.result
