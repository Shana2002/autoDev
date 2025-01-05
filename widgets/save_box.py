import customtkinter as ctk

class SaveBox:
    def __init__(self, parent, actions, name):
        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title("Save Preset")
        self.dialog.geometry('400x200')
        self.dialog.transient(parent)
        self.dialog.grab_set()
        self.dialog.resizable(False, False)
        self.actions = actions

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
        """Handle the save action and close the dialog."""
        if self.save_name.get():
            try:
                with open(f"presets/{self.save_name.get()}.txt", "w") as f:
                    for action in self.actions:
                        print(action)  # For debugging purposes
                        f.write(str(action))
                        f.write('\n')
            except Exception as e:
                print(e)
            finally:
                self.dialog.destroy()
            
        self.result = self.save_name.get()
        self.dialog.destroy()

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result


# # Example usage (ensure customtkinter is initialized before using CTk widgets):
# if __name__ == "__main__":
#     import tkinter as tk

#     # Initialize customtkinter (theme setting is optional)
#     ctk.set_appearance_mode("System")
#     ctk.set_default_color_theme("blue")

#     root = tk.Tk()
#     root.geometry("300x200")

#     # Dummy actions
#     actions = [{"action": "example"}]

#     def open_dialog():
#         dialog = SaveBox(root, actions, "PresetName")
#         result = dialog.show()
#         if result:
#             print("Saved As:", result)

#     open_dialog_btn = ctk.CTkButton(root, text="Open Save Dialog", font=("Helvetica", 12), command=open_dialog)
#     open_dialog_btn.pack(pady=50)

#     root.mainloop()
