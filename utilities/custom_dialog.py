from tkinter import *
from tkinter import ttk


class CustomDialog:
    def __init__(self, parent, title="Dialog", message="Enter action details:"):
        self.dialog = Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("600x500")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)

        # Initialize variables
        self.action_type_var = StringVar(value="click")
        self.path_type_var = StringVar(value="xpath")
        self.path_var = StringVar()
        self.value_var = StringVar()
        self.use_database_var = BooleanVar(value=False)
        self.selected_table_var = StringVar()
        self.selected_column_var = StringVar()

        # Return value
        self.result = None

        # Main Frame
        main_frame = Frame(self.dialog, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Title and Description
        title_label = Label(main_frame, text=message, font=("Helvetica", 14, "bold"), anchor="center")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Action Type Selection
        action_type_label = Label(main_frame, text="Select Action Type:", font=("Helvetica", 12))
        action_type_label.grid(row=1, column=0, sticky="w", pady=5)

        self.action_type_menu = ttk.Combobox(main_frame, textvariable=self.action_type_var, width=25)
        self.action_type_menu['values'] = ["click", "send data"]
        self.action_type_menu.grid(row=1, column=1, pady=5)
        self.action_type_menu.current(0)
        self.action_type_menu.bind("<<ComboboxSelected>>", self.update_fields)  # Bind event

        # Path Type Selection
        path_type_label = Label(main_frame, text="Select Path Type:", font=("Helvetica", 12))
        path_type_label.grid(row=2, column=0, sticky="w", pady=5)

        self.path_type_menu = ttk.Combobox(main_frame, textvariable=self.path_type_var, width=25)
        self.path_type_menu['values'] = ["xpath", "id", "class"]
        self.path_type_menu.grid(row=2, column=1, pady=5)
        self.path_type_menu.current(0)

        # Path Entry
        path_label = Label(main_frame, text="Enter Path:", font=("Helvetica", 12))
        path_label.grid(row=3, column=0, sticky="w", pady=5)

        self.path_entry = Entry(main_frame, textvariable=self.path_var, width=28, font=("Helvetica", 10))
        self.path_entry.grid(row=3, column=1, pady=5)

        # Toggle Buttons for Value
        self.manual_button = Radiobutton(main_frame, text="Manual Entry", variable=self.use_database_var,
                                          value=False, command=self.update_value_fields, font=("Helvetica", 12))
        self.database_button = Radiobutton(main_frame, text="From Database", variable=self.use_database_var,
                                           value=True, command=self.update_value_fields, font=("Helvetica", 12))

        # Value Section
        self.value_label = Label(main_frame, text="Enter Value:", font=("Helvetica", 12))
        self.value_entry = Entry(main_frame, textvariable=self.value_var, width=28, font=("Helvetica", 10))

        # Database Section
        self.table_label = Label(main_frame, text="Select Table:", font=("Helvetica", 12))
        self.table_menu = ttk.Combobox(main_frame, textvariable=self.selected_table_var, width=25, state="readonly")
        self.table_menu['values'] = ["users", "products", "orders"]  # Replace with dynamic database fetch
        self.table_menu.bind("<<ComboboxSelected>>", self.update_columns)

        self.column_label = Label(main_frame, text="Select Column:", font=("Helvetica", 12))
        self.column_menu = ttk.Combobox(main_frame, textvariable=self.selected_column_var, width=25, state="readonly")

        # Buttons
        button_frame = Frame(self.dialog)
        button_frame.pack(pady=10)

        self.ok_button = Button(button_frame, text="OK", font=("Helvetica", 12), bg="#4CAF50", fg="white",
                                width=12, command=self.on_ok)
        self.ok_button.pack(side=LEFT, padx=5)

        self.cancel_button = Button(button_frame, text="Cancel", font=("Helvetica", 12), bg="#F44336", fg="white",
                                    width=12, command=self.on_cancel)
        self.cancel_button.pack(side=LEFT, padx=5)

        # Show Default Fields
        self.update_fields()

    def update_fields(self, event=None):
        """Show or hide fields based on the selected action type."""
        if self.action_type_var.get() == "send data":
            self.manual_button.grid(row=4, column=0, sticky="w", pady=5)
            self.database_button.grid(row=4, column=1, pady=5)
            self.update_value_fields()
        else:
            self.manual_button.grid_forget()
            self.database_button.grid_forget()
            self.value_label.grid_forget()
            self.value_entry.grid_forget()
            self.table_label.grid_forget()
            self.table_menu.grid_forget()
            self.column_label.grid_forget()
            self.column_menu.grid_forget()

    def update_value_fields(self):
        """Update value fields based on toggle selection."""
        if self.use_database_var.get():
            self.value_label.grid_forget()
            self.value_entry.grid_forget()
            self.table_label.grid(row=5, column=0, sticky="w", pady=5)
            self.table_menu.grid(row=5, column=1, pady=5)
            self.column_label.grid(row=6, column=0, sticky="w", pady=5)
            self.column_menu.grid(row=6, column=1, pady=5)
        else:
            self.table_label.grid_forget()
            self.table_menu.grid_forget()
            self.column_label.grid_forget()
            self.column_menu.grid_forget()
            self.value_label.grid(row=5, column=0, sticky="w", pady=5)
            self.value_entry.grid(row=5, column=1, pady=5)

    def update_columns(self, event=None):
        """Update column options based on the selected table."""
        table_columns = {
            "users": ["id", "name", "email"],
            "products": ["id", "name", "price"],
            "orders": ["id", "user_id", "total"],
        }
        selected_table = self.selected_table_var.get()
        self.column_menu['values'] = table_columns.get(selected_table, [])
        if self.column_menu['values']:
            self.column_menu.current(0)

    def on_ok(self):
        """Collect data and close the dialog."""
        if self.action_type_var.get() == "send data":
            value = {
                "table": self.selected_table_var.get(),
                "column": self.selected_column_var.get()
            } if self.use_database_var.get() else self.value_var.get()
        else:
            value = None

        self.result = {
            "function": self.action_type_var.get(),
            "type": self.path_type_var.get(),
            "path": self.path_var.get(),
            "value": value,
        }
        self.dialog.destroy()

    def on_cancel(self):
        """Cancel and close the dialog."""
        self.result = None
        self.dialog.destroy()

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result


# # Example Usage
# if __name__ == "__main__":
#     def open_dialog():
#         dialog = CustomDialog(root, title="Enhanced Action Dialog")
#         result = dialog.show()
#         if result:
#             print("Action Result:", result)

#     root = Tk()
#     root.geometry("300x200")

#     open_dialog_btn = Button(root, text="Open Dialog", command=open_dialog, font=("Helvetica", 12), bg="#2196F3", fg="white")
#     open_dialog_btn.pack(pady=50)

#     root.mainloop()
