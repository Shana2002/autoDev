from tkinter import *
from tkinter import ttk
from custom_dialog import CustomDialog


class Main:
    def __init__(self, root):
        # Variables
        self.actions = []
        # Main Frame
        self.root = root
        self.root.geometry("800x640+0+0")
        self.root.config(bg="#23252D")

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

        count_var = IntVar()
        count_entry = Entry(frame1, width=15, textvariable=count_var)
        count_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # URL entry 
        url_lable = Label(root, text="Enter Url: ", font=("Helvetica", 12), fg="white", bg="#23252D")
        url_lable.pack(side="top", pady=1)
        url_var = StringVar()
        url_entry = Entry(root,width=100,textvariable=url_var)
        url_entry.pack(side="top", pady=2)

        # Main action frame with scrollable canvas
        canvas_frame = Frame(root, bg="white", width=500, height=300)
        canvas_frame.pack(side="top", pady=10)

        self.canvas = Canvas(canvas_frame, bg="white", width=480, height=300)
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

        self.main_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Add action button
        btn_add = Button(root, text="Click me", command=self.add_event)
        btn_add.pack(side="top", pady=10)

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

            for action in self.actions:
                # Create a new sub-frame for each action
                sub_frame = Frame(self.main_frame, bg="yellow", width=300, height=50)
                sub_frame.pack(pady=5, padx=10, anchor="w")
                
                # Add a label with action details
                Label(sub_frame, text=f"{action['path']}", bg="yellow").pack()

                # Increment the count
                self.count += 1

            # Update the canvas scrollregion to accommodate new widgets
            self.canvas.update_idletasks()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        


if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
