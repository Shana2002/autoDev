from tkinter import *


class SaveBox:
    def __init__(self, parent,actions):
        self.dialog = Toplevel(parent)
        self.dialog.title("Save Preset")
        self.dialog.geometry('400x200')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)
        self.actions = actions

        # Initialize variables
        self.save_name = StringVar()
        self.result = None

        # Center Frame for alignment
        frame = Frame(self.dialog)
        frame.pack(expand=True)

        # UI Implementation
        # Save Name
        Label(frame, text="Save Name:", font=("Helvetica", 12)).grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Entry(frame, textvariable=self.save_name, font=("Helvetica", 12), width=30).grid(column=1, row=0, padx=10, pady=10, sticky="w")

        # Buttons
        save_button = Button(frame, text="Save", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.save)
        save_button.grid(column=0, row=1, padx=10, pady=20, columnspan=2, sticky="n")

    # Functions
    def save(self):
        """Handle the save action and close the dialog."""

        if self.save_name.get():
            try:
                f = open(f"presets/{self.save_name.get()}.txt","w")
                for action in self.actions:
                    print(action)
                    f.write(str(action))
                    f.write('\n')
                f.close()
            except:
                pass
            finally:
                self.dialog.destroy()
            # file check
            
        self.result = self.save_name.get()
        self.dialog.destroy()

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result


# actions = [
#     {"function":"click","type":"xpath","path":'/html/body/div[1]/div/div[3]/a[1]/i',"value":"hansaka"},
#     {"function":"send_key","type":"xpath","path":'//*[@id="username"]',"value":"hansaka"},
#     {"function":"send_key","type":"xpath","path":'//*[@id="password"]',"value":"hansaka"},
#     {"function":"click","type":"xpath","path":'//*[@id="login-form"]/div[2]/div[2]/div[1]/form/input',"value":"hansaka"},
#     ]


# if __name__ == "__main__":
#     def open_dialog():
#         dialog = SaveBox(root,actions)
#         result = dialog.show()
#         if result:
#             print("Action Result:", result)

#     root = Tk()
#     root.geometry("300x200")

#     open_dialog_btn = Button(root, text="Open Dialog", command=open_dialog, font=("Helvetica", 12), bg="#2196F3", fg="white")
#     open_dialog_btn.pack(pady=50)

#     root.mainloop()
