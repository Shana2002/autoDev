from tkinter import *
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utilities import db


class Settings:
    def __init__(self, parent):
        self.dialog = Toplevel(parent)
        self.dialog.title("Settings")
        self.dialog.geometry('300x200')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)

        # UI Implementation
        Label(self.dialog, text="Settings", font=("Helvetica", 14)).pack(pady=10)

        reset_button = Button(self.dialog, text="Reset Database", font=("Helvetica", 12), bg="#F44336", fg="white", command=self.reset_database)
        reset_button.pack(pady=10)

        show_db_button = Button(self.dialog, text="Show Database", font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.show_database)
        show_db_button.pack(pady=10)

    def reset_database(self):
        """Handle the database reset action."""
        db.reset_db()
        self.dialog.destroy()

    def show_database(self):
        """Handle the show database action."""
        os.system("start explorer .")  # Open current directory as a placeholder for showing database

# Example usage
if __name__ == "__main__":
    def open_settings():
        settings = Settings(root)

    root = Tk()
    root.geometry("300x200")

    settings_btn = Button(root, text="Settings", command=open_settings, font=("Helvetica", 12), bg="#FF9800", fg="white")
    settings_btn.pack(pady=10)

    root.mainloop()
