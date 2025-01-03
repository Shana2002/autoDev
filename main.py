from tkinter import *
from tkinter import ttk,messagebox
from utilities.custom_dialog import CustomDialog
from run import Run
from widgets.save_box import SaveBox
from widgets.load_box import LoadBox
from widgets.setting_box import Settings




class Main:
    def __init__(self, root):
        # Variables
        self.actions = []
        # Main Frame
        self.root = root
        self.root.geometry("800x640+0+0")
        self.root.config(bg="#23252D")
        self.save_name = ""
        # Title in Window
        self.root.title("Auto Dev - Testing unit >> developed by hansaka")
        label1 = Label(
            root,
            text="Welcome to autoDev",
            font=("Helvetica", 20, "bold"),
            bg="#23252D",
            fg="white",
            anchor="center",
        )
        label1.pack(side="top", pady=20)

        # Counter Frame
        frame1 = Frame(root, bg="#23252D")
        frame1.pack(side="top", pady=10)

        # Label and Entry on the same line
        label2 = Label(
            frame1, text="Enter Count: ", font=("Helvetica", 12), fg="white", bg="#23252D"
        )
        label2.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        count_var = IntVar(value=10)
        count_entry = Entry(frame1, width=15, textvariable=count_var)
        count_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # URL entry 
        url_lable = Label(root, text="Enter Url: ", font=("Helvetica", 12), fg="white", bg="#23252D")
        url_lable.pack(side="top", pady=1)
        url_var = StringVar()
        url_entry = Entry(root,width=100,textvariable=url_var)
        url_entry.pack(side="top", pady=2)

        # Main action frame with scrollable canvas
        canvas_frame = Frame(root, bg="#23252D", width=500, height=300)
        canvas_frame.pack(side="top", pady=10)

        self.canvas = Canvas(canvas_frame, bg="#23252D", width=480, height=300)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            canvas_frame, orient="vertical", command=self.canvas.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.main_frame = Frame(self.canvas, bg="red",width=480)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Add action button
        btn_add = Button(root, text="Click me", command=self.add_event)
        btn_add.pack(side="top", pady=10)

        # Add action button
        btn_add = Button(root, text="Run", command=lambda: self.run_action(count_var, url_var))
        btn_add.pack(side="top", pady=10)

        # save button
        btn_add = Button(root, text="Save", command=self.save_frame)
        btn_add.place(x=600,y=20)

        # load button
        btn_add = Button(root, text="Load", command=self.load_frame)
        btn_add.place(x=650,y=20)

        # setting button
        btn_add = Button(root, text="Setting", command=self.add_event)
        btn_add.place(x=700,y=20)

    def add_event(self):
        dialog = CustomDialog(root)
        result = dialog.show()
        if result:
            self.actions.append(result)
            self.create_subframe()

    def create_subframe(self):
        """Create sub-frames dynamically based on actions and manage scroll region."""
        if self.actions:
            # Clear the main_frame children before adding new ones
            for widget in self.main_frame.winfo_children():
                widget.destroy()

            for i, action in enumerate(self.actions):
                # Create a new sub-frame for each action
                sub_frame = Frame(self.main_frame, bg="#f0f0f0", bd=2, relief="groove", padx=10, pady=5,)
                sub_frame.pack(pady=5, padx=10, anchor="w")

                # Path Label
                Label(sub_frame, text=f"function: {action['function']}", font=("Helvetica", 10, "bold"), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5)

                # Path Label
                Label(sub_frame, text=f"Path: {action['path']}", font=("Helvetica", 10, "bold"), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5)
                
                # Path Label
                Label(sub_frame, text=f"Path: {action['path']}", font=("Helvetica", 10, "bold"), bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=5)

                # Value Label
                Label(sub_frame, text=f"Value: {action.get('value', 'N/A')}", font=("Helvetica", 10), bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=5)

                # Delete Button
                delete_button = Button(sub_frame, text="Delete", bg="#FF6347", fg="white", font=("Helvetica", 10, "bold"), command=lambda a=action: self.delete_action(a))
                delete_button.grid(row=0, column=1, rowspan=2, padx=10, sticky="e")

                # Edit Button
                edit_button = Button(sub_frame, text="Edit", bg="#4682B4", fg="white", font=("Helvetica", 10, "bold"), command=lambda a=action: self.edit_action(a))
                edit_button.grid(row=0, column=2, rowspan=2, padx=5, sticky="e")

                # Up Button
                if i > 0:  # Disable for the first item
                    up_button = Button(sub_frame, text="▲", bg="#32CD32", fg="white", font=("Helvetica", 10, "bold"), command=lambda index=i: self.move_action(index, -1))
                    up_button.grid(row=0, column=3, rowspan=2, padx=5, sticky="e")

                # Down Button
                if i < len(self.actions) - 1:  # Disable for the last item
                    down_button = Button(sub_frame, text="▼", bg="#FFA500", fg="white", font=("Helvetica", 10, "bold"), command=lambda index=i: self.move_action(index, 1))
                    down_button.grid(row=0, column=4, rowspan=2, padx=5, sticky="e")

            # Update the canvas scrollregion to accommodate new widgets
            self.canvas.update_idletasks()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def move_action(self, index, direction):
        """Move an action up or down in the list and refresh the sub-frames."""
        new_index = index + direction
        if 0 <= new_index < len(self.actions):
            # Swap the actions
            self.actions[index], self.actions[new_index] = self.actions[new_index], self.actions[index]
            # Refresh the UI
            self.create_subframe()
    
    def run_action(self,count_var,url_var):
        if count_var.get()>0 and url_var.get()!="" and len(self.actions)>0:
            run_status = Run(self.root,count_var.get(),url_var.get(),self.actions)

    def save_frame(self):
        if len(self.actions)==0:
            messagebox.showerror('Error','No actions to save please add actions and save')
            return
        dialog = SaveBox(root,self.actions,self.save_name)
        result = dialog.show()
        
    def load_frame(self):
        if len(self.actions)>=0:
            res = messagebox.askquestion('Do you want Proceeed?','Alredy you add actions when you load your previous action will delete , Do you want proceed')
            if res == 'yes':
                dilaog = LoadBox(self.root,self.actions)
                result = dilaog.show()
                if isinstance(result,dict):
                    self.actions.clear()
                    self.actions = result["result"]
                    self.save_name = result["name"]
                    self.create_subframe()
                    return
                messagebox.showerror('Error','Something error if your saved file get damaged or saved file not like file type')
                return



if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
