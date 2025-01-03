from tkinter import *
import os

class LoadBox:
    def __init__(self, parent, actions):
        self.dialog = Toplevel(parent)
        self.dialog.title("Load Preset")
        self.dialog.geometry('400x300')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)
        self.actions = actions
        self.result = None

        # Files list
        self.files = self.list_files()

        # UI Implementation
        Label(self.dialog, text="Available Presets:", font=("Helvetica", 12)).pack(pady=10)

        # Listbox to display files
        self.file_listbox = Listbox(self.dialog, font=("Helvetica", 12), width=40, height=10)
        self.file_listbox.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Populate Listbox
        for file in self.files:
            self.file_listbox.insert(END, file)

        # Buttons
        load_button = Button(self.dialog, text="Load", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.load)
        load_button.pack(side=LEFT, padx=20, pady=10)

        cancel_button = Button(self.dialog, text="Cancel", font=("Helvetica", 12), bg="#F44336", fg="white", command=self.dialog.destroy)
        cancel_button.pack(side=RIGHT, padx=20, pady=10)

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result

    def list_files(self):
        """List files in the 'presets' directory."""
        path = "presets"
        if not os.path.exists(path):
            os.makedirs(path)
        return os.listdir(path)

    def load(self):
        """Handle the load action."""
        selected_file = self.file_listbox.get(ACTIVE)
        if selected_file:
            self.result = {}
            self.res = []
            f = open(f"presets/{selected_file}","r")
            for line in f:
                action = line.replace('\n',"")
                convert = eval(action)
                
                self.res.append(convert)
            self.result["result"]=self.res
            self.result["name"]=selected_file
            self.dialog.destroy()
            

# Example usage
# if __name__ == "__main__":

#     actions = []
#     print(actions)


#     def open_dialog():
#         dialog = LoadBox(root, None)
#         result = dialog.show()
#         if result:
#             print("Selected File:", result[0]['type'])

#     root = Tk()
#     root.geometry("300x200")
    
#     open_dialog_btn = Button(root, text="Open Dialog", command=open_dialog, font=("Helvetica", 12), bg="#2196F3", fg="white")
#     open_dialog_btn.pack(pady=50)

#     root.mainloop()