from tkinter import *
from tkinter import ttk

class CustomDialog:
    def __init__(self, parent, title="Dialog", message="Enter action details:"):
        # Create a top-level window
        self.dialog = Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("500x400")
        self.dialog.transient(parent)  # Ensure dialog is on top of parent
        self.dialog.grab_set()  # Block interaction with parent window
        self.dialog.resizable(False, False)

        # Initialize variables
        self.action_type_var = StringVar()
        self.path_type_var = StringVar()
        self.path_var = StringVar()
        self.value_var = StringVar()

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
        self.action_type_menu.current(0)  # Default to "click"

        # Path Type Selection
        path_type_label = Label(main_frame, text="Select Path Type:", font=("Helvetica", 12))
        path_type_label.grid(row=2, column=0, sticky="w", pady=5)

        self.path_type_menu = ttk.Combobox(main_frame, textvariable=self.path_type_var, width=25)
        self.path_type_menu['values'] = ["xpath", "id", "class"]
        self.path_type_menu.grid(row=2, column=1, pady=5)
        self.path_type_menu.current(0)  # Default to "xpath"

        # Path Entry
        path_label = Label(main_frame, text="Enter Path:", font=("Helvetica", 12))
        path_label.grid(row=3, column=0, sticky="w", pady=5)

        self.path_entry = Entry(main_frame, textvariable=self.path_var, width=28, font=("Helvetica", 10))
        self.path_entry.grid(row=3, column=1, pady=5)

        # Value Entry (Visible only if action type is "send data")
        self.value_label = Label(main_frame, text="Enter Value:", font=("Helvetica", 12))
        self.value_entry = Entry(main_frame, textvariable=self.value_var, width=28, font=("Helvetica", 10))

        # Show/Hide Value Entry based on Action Type
        self.action_type_var.trace_add("write", self.toggle_value_entry)

        # Buttons
        button_frame = Frame(self.dialog)
        button_frame.pack(pady=10)

        self.ok_button = Button(button_frame, text="OK", font=("Helvetica", 12), bg="#4CAF50", fg="white", 
                                width=12, command=self.on_ok)
        self.ok_button.pack(side=LEFT, padx=5)

        self.cancel_button = Button(button_frame, text="Cancel", font=("Helvetica", 12), bg="#F44336", fg="white",
                                    width=12, command=self.on_cancel)
        self.cancel_button.pack(side=LEFT, padx=5)

        # Style and Tooltips
        self.add_tooltips()

    def toggle_value_entry(self, *args):
        """Show or hide the Value entry field based on the action type."""
        if self.action_type_var.get() == "send data":
            self.value_label.grid(row=4, column=0, sticky="w", pady=5)
            self.value_entry.grid(row=4, column=1, pady=5)
        else:
            self.value_label.grid_forget()
            self.value_entry.grid_forget()

    def on_ok(self):
        """Collect data and close the dialog."""
        self.result = {
            "function": self.action_type_var.get(),
            "type": self.path_type_var.get(),
            "path": self.path_var.get(),
            "value": self.value_var.get() if self.action_type_var.get() == "send data" else None,
        }
        self.dialog.destroy()

    def on_cancel(self):
        """Cancel and close the dialog."""
        self.result = None
        self.dialog.destroy()

    def add_tooltips(self):
        """Add tooltips for better user guidance."""
        self.path_entry_tooltip = ToolTip(self.path_entry, text="Enter the locator path (e.g., XPath, ID).")
        self.value_entry_tooltip = ToolTip(self.value_entry, text="Value to send (only for 'send data').")

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result


class ToolTip:
    """Create a tooltip for a widget."""
    def __init__(self, widget, text="Tooltip"):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = Toplevel(self.widget)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.geometry(f"+{x}+{y}")
        label = Label(self.tip_window, text=self.text, justify="left",
                      background="#FFFFE0", relief="solid", borderwidth=1,
                      font=("Helvetica", 10))
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


# Example Usage
if __name__ == "__main__":
    def open_dialog():
        dialog = CustomDialog(root, title="Enhanced Action Dialog")
        result = dialog.show()
        if result:
            actions.append(result)
            print("Action Added:", result)

    actions = []
    root = Tk()
    root.geometry("300x200")

    open_dialog_btn = Button(root, text="Open Dialog", command=open_dialog, font=("Helvetica", 12), bg="#2196F3", fg="white")
    open_dialog_btn.pack(pady=50)

    root.mainloop()
