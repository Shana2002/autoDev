import customtkinter as ctk
import os
from models.Store import Store

class LoadBox:
    def __init__(self, parent, actions):
        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Load Preset")
        self.dialog.geometry('300x450')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)
        self.actions = actions
        self.result = None
        self.file_name = None

        # Files list
        self.files = self.list_files()

        # UI Implementation
        self.title_label = ctk.CTkLabel(self.dialog, text="Available Presets:", font=("Helvetica", 14))
        self.title_label.pack(pady=10)

        # Scrollable Frame to hold the labels (file names)
        self.scrollable_frame = ctk.CTkScrollableFrame(self.dialog)
        self.scrollable_frame.pack(padx=20, pady=10, fill=ctk.BOTH, expand=True)

        # Labels for file names
        self.file_labels = []
        for file in self.files:
            label = ctk.CTkLabel(self.scrollable_frame, text=file, font=("Helvetica", 12), anchor="w", width=300, height=30)
            label.pack(fill=ctk.X, pady=5)
            label.bind("<Button-1>", lambda e, f=file, l=label: self.select_file(e, f, l))
            self.file_labels.append(label)

        # Buttons (using CTkButton from customtkinter)
        self.button_frame = ctk.CTkFrame(self.dialog)  # Frame for buttons to align them nicely
        self.button_frame.pack(pady=10)

        self.load_button = ctk.CTkButton(self.button_frame, text="Load", font=("Helvetica", 12), command=self.load)
        self.load_button.pack(side=ctk.LEFT, padx=20)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", font=("Helvetica", 12), command=self.dialog.destroy)
        self.cancel_button.pack(side=ctk.RIGHT, padx=20)

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result

    def list_files(self):
        """List files in the 'presets' directory."""
        path = "presets"
        if not os.path.exists(path):
            os.makedirs(path)
        file_names = os.listdir(path)
        file_names = list(map(lambda name: name.replace('.txt',''),file_names))
        return file_names

    def load1(self):
        """Handle the load action."""
        if self.result:
            selected_file = self.result["name"]
            self.result = {}
            self.res = []
            try:
                with open(f"presets/{selected_file}.txt", "r") as f:
                    for line in f:
                        action = line.replace('\n', "")
                        convert = eval(action)
                        self.res.append(convert)
                self.result["result"] = self.res
                self.result["name"] = selected_file
            except Exception as e:
                print(e)
                return self.result
            self.dialog.destroy()

    def load(self):
        if self.file_name:
            result = Store().load(self.file_name)
            if result:
                self.result = result
            self.dialog.destroy()

    def select_file(self, event, file_name, label):
        """Handle file selection and change label color."""
        # Reset the background color of all labels to default (transparent)
        for lbl in self.file_labels:
            lbl.configure(bg_color="transparent", fg_color="transparent")  # Use 'transparent' instead of None

        # Change background color of selected label
        label.configure(bg_color="#4CAF50", fg_color="blue")

        # Save the selected file name in the result
        # self.result = {"name": file_name}
        self.file_name = file_name


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