import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Auto Dev")
        self.geometry("800x600")
        
        # Configure grid layout for the root window
        self.columnconfigure(0, weight=1)  # Center column expands
        self.rowconfigure(0, weight=1)     # Name label row
        self.rowconfigure(1, weight=1)     # Main frame row

        # name label
        name_label = customtkinter.CTkLabel(
            self, 
            text="Welcome to Auto Dev", 
            font=customtkinter.CTkFont(size=30, weight="bold")
        )
        name_label.grid(column=0, row=0, pady=10)

        # main frame design
        self.main_frame = customtkinter.CTkFrame(self, width=750, height=450)
        self.main_frame.grid(column=0, row=1, pady=20, sticky="n")  # Adjusted alignment

        # Center alignment for the main_frame
        self.main_frame.grid_propagate(False)  # Prevent resizing to contents
        # self.main_frame.grid_columnconfigure((2, 3), weight=0)
        # self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # add button
        self.add_btn  = customtkinter.CTkButton(self.main_frame,text="Add",width=500)
        self.add_btn.grid(row=0,column=0,pady=10,padx=5)

        # action frame
        self.action_frame = customtkinter.CTkScrollableFrame(self.main_frame,width=480 , height=370)
        self.action_frame.grid(row=1,column=0,pady=10,padx=5)

        # sub frame
        self.subframe = customtkinter.CTkFrame(self.main_frame,width=215,height=430)
        self.subframe.grid(row=0,column=1,rowspan=2,pady=10,padx=5)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
