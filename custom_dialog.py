from tkinter import *

class CustomDialog:
    def __init__(self, parent, title="Dialog", message="Enter a value:"):
        # Create a top-level window
        self.dialog = Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("300x150")
        self.dialog.transient(parent)  # Ensure dialog is on top of parent
        self.dialog.grab_set()  # Block interaction with parent window

        # Message Label
        self.message_label = Label(self.dialog, text=message, font=("Helvetica", 12))
        self.message_label.pack(pady=10)

        # Entry field for input
        self.input_var = StringVar()
        self.entry = Entry(self.dialog, textvariable=self.input_var, width=30)
        self.entry.pack(pady=5)

        # Buttons
        self.button_frame = Frame(self.dialog)
        self.button_frame.pack(pady=10)

        self.ok_button = Button(self.button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side=LEFT, padx=5)

        self.cancel_button = Button(self.button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side=LEFT, padx=5)

        # Initialize the return value
        self.value = None

    def on_ok(self):
        self.value = self.input_var.get()  # Retrieve the entered value
        self.dialog.destroy()  # Close the dialog

    def on_cancel(self):
        self.value = None  # Set the value to None
        self.dialog.destroy()  # Close the dialog

    def show(self):
        self.dialog.wait_window()  # Wait for the dialog to close
        return self.value  # Return the user input or None