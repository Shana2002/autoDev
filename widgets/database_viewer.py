from tkinter import *
from tkinter import ttk
class DatabaseViewer:
    def __init__(self, parent):
        self.dialog = Toplevel(parent)
        self.dialog.title("Database Viewer")
        self.dialog.geometry('600x500')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)

        # UI Implementation
        Label(self.dialog, text="Database Viewer", font=("Helvetica", 14)).pack(pady=10)

        self.selector_frame = Frame(self.dialog)
        self.selector_frame.pack(pady=10)

        self.table_selector = ttk.Combobox(self.selector_frame, state="readonly", values=self.get_table_list())
        self.table_selector.pack(side=LEFT, padx=5)
        self.table_selector.bind("<<ComboboxSelected>>", self.update_table)

        self.load_button = Button(self.selector_frame, text="Load Table", command=self.update_table, font=("Helvetica", 10), bg="#4CAF50", fg="white")
        self.load_button.pack(side=LEFT, padx=5)

        self.table_frame = Frame(self.dialog)
        self.table_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

        self.populate_table([])  # Initialize with empty data

    def get_table_list(self):
        """Retrieve the list of tables (dummy data for now)."""
        # Replace this with actual database table retrieval logic
        return ["Table1", "Table2", "Table3"]

    def populate_table(self, data):
        """Populate the table with database data."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        if not data:
            columns = ("No Data",)
            data = [("Select a table to load data",)]
        else:
            columns = data[0]
            data = data[1:]

        # Create Treeview
        tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")

        # Define headings
        for col in columns:
            tree.heading(col, text=col)

        # Insert data
        for row in data:
            tree.insert("", END, values=row)

        tree.pack(fill=BOTH, expand=True)

    def update_table(self, event=None):
        """Update the table data based on the selected table."""
        selected_table = self.table_selector.get()
        if selected_table:
            # Replace this with actual database query logic for the selected table
            if selected_table == "Table1":
                data = [("ID", "Name", "Value"), (1, "Item1", "Value1"), (2, "Item2", "Value2")]
            elif selected_table == "Table2":
                data = [("ID", "Category", "Description"), (1, "Cat1", "Desc1"), (2, "Cat2", "Desc2")]
            else:
                data = [("Column1", "Column2"), ("Data1", "Data2")]
            self.populate_table(data)

# Example usage
if __name__ == "__main__":
    def open_settings():
        settings = DatabaseViewer(root)

    root = Tk()
    root.geometry("300x200")

    settings_btn = Button(root, text="Settings", command=open_settings, font=("Helvetica", 12), bg="#FF9800", fg="white")
    settings_btn.pack(pady=10)

    root.mainloop()

