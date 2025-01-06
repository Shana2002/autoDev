import customtkinter as ctk
from models.Store import Store

class SaveBox:
    def __init__(self, parent, actions, name,url):
        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Save Preset")
        self.dialog.geometry('400x200')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)
        self.actions = actions
        self.url = url

        # Initialize variables
        self.save_name = ctk.StringVar(value=name)
        self.result = None

        # Center Frame for alignment
        frame = ctk.CTkFrame(self.dialog)
        frame.pack(expand=True)

        # UI Implementation

        save_entry = ctk.CTkEntry(frame, textvariable=self.save_name, font=("Helvetica", 12), width=200)
        save_entry.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Buttons
        save_button = ctk.CTkButton(frame, text="Save", font=("Helvetica", 12), command=self.save, width=15)
        save_button.grid(column=0, row=1, padx=10, pady=20, columnspan=2, sticky="nsew")

    def save(self):
        self.result = Store().save(self.save_name.get(),self.actions,self.url)
        self.dialog.destroy()
        

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result

