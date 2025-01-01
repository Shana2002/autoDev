from tkinter import *
from custom_dialog import CustomDialog

class Main:
    def __init__(self, root):
        # Variables
        count_var = IntVar()
        self.count = 0
        # Main Frame
        self.root = root
        self.root.geometry("800x640+0+0")
        self.root.config(bg="#23252D")
        
        # Title in Window
        self.root.title("Auto Dev - Testing unit >> developed by hansaka")
        label1 = Label(root, text="Welcome to autoDev", font=("Helvetica", 20, "bold"), bg="#23252D", fg="white", anchor="center")
        label1.pack(side="top", pady=20)

        # Counter Frame
        frame1 = Frame(root, bg="#23252D")
        frame1.pack(side="top", pady=10)

        # Label and Entry on the same line
        label2 = Label(frame1, text="Enter Count: ", font=("Helvetica", 12), fg="white", bg="#23252D")
        label2.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        count_entry = Entry(frame1, width=15, textvariable=count_var)
        count_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Add action button
        btn_add = Button(root,text="Click me",command=self.add_event,)
        btn_add.pack(side="top", pady=10)

        # Main action Frame
        self.main_frame = Frame(root,bg="white",width=500,)
        self.main_frame.pack(side="top", pady=10)

        # Action Details
        # sub_frame = Frame(self.main_frame,bg="yellow",width=300,height=50)
        # sub_frame.grid(row=0,column=0,padx=10, pady=5, sticky="w")

    def add_event(self):
        event_dialog = CustomDialog(self.root)
        sub_frame = Frame(self.main_frame,bg="yellow",width=300,height=50)
        sub_frame.grid(row=self.count,column=0,padx=10, pady=5, sticky="w")
        self.count += 1



if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
