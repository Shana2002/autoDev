import customtkinter
from widgets.add_action import AddAction
from widgets.load_box import LoadBox

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Auto Dev")
        self.geometry("800x600")
        self.actions = []
        
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
        self.add_btn  = customtkinter.CTkButton(self.main_frame,text="Add",width=500,command=self.add_action_tab)
        self.add_btn.grid(row=0,column=0,pady=10,padx=5)

        # action frame
        self.action_frame = customtkinter.CTkScrollableFrame(self.main_frame,width=480 , height=370)
        self.action_frame.grid(row=1,column=0,pady=10,padx=5)

        # Subframe
        self.subframe = customtkinter.CTkFrame(self.main_frame, width=215, height=430)
        self.subframe.grid(row=0, column=1, rowspan=2, pady=10, padx=5)
        self.subframe.grid_propagate(False)

        # Configure grid for subframe
        self.subframe.rowconfigure(0, weight=10)  # Give the 'Run' button more space
        self.subframe.rowconfigure((1, 2, 3), weight=1)  # Equal weight for Save, Load, and Log
        self.subframe.columnconfigure(0, weight=1)  # Center-align buttons

        # Run Button (larger size)
        self.run_button = customtkinter.CTkButton(self.subframe, text="Run", width=200, height=40)
        self.run_button.grid(row=0, column=0, pady=10, padx=10)

        # Save Button
        self.save_button = customtkinter.CTkButton(self.subframe, text="Save", width=200, height=40)
        self.save_button.grid(row=1, column=0, pady=10, padx=10)

        # Load Button
        self.load_button = customtkinter.CTkButton(self.subframe, text="Load", width=200, height=40,command=self.load_presets)
        self.load_button.grid(row=2, column=0, pady=10, padx=10)

        # setting Button
        self.setting_button = customtkinter.CTkButton(self.subframe, text="Setting", width=200, height=40)
        self.setting_button.grid(row=3, column=0, pady=10, padx=10)




        for x in range(1, 10):
            self.create_actions()
        
        
    def create_actions(self):
        self.action_card = customtkinter.CTkFrame(self.action_frame, width=480, height=160)
        self.action_card.pack(pady=5)
        self.action_card.grid_propagate(False)

        # Card title
        title = customtkinter.CTkLabel(
            self.action_card,
            text="Click Login Button ",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            justify="left",
            anchor="w"
        )
        title.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=5)

        # Action Details
        do_function = customtkinter.CTkLabel(self.action_card, text="Action: Click")
        do_function.grid(row=1, column=0, sticky="w", padx=10, pady=2)

        path = customtkinter.CTkLabel(self.action_card, text="Path: /login/button")
        path.grid(row=2, column=0, sticky="w", padx=10, pady=2)

        # Value Field
        value_label = customtkinter.CTkLabel(self.action_card, text="Value:")
        value_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Action Buttons
        edit_button = customtkinter.CTkButton(self.action_card, text="Edit", width=70)
        edit_button.grid(row=1, column=2, padx=5, pady=5)

        delete_button = customtkinter.CTkButton(self.action_card, text="Delete", width=70)
        delete_button.grid(row=1, column=3, padx=5, pady=5)

        up_button = customtkinter.CTkButton(self.action_card, text="Up", width=70)
        up_button.grid(row=2, column=2, padx=5, pady=5)

        down_button = customtkinter.CTkButton(self.action_card, text="Down", width=70)
        down_button.grid(row=2, column=3, padx=5, pady=5)

        # Adjust the grid proportions within the card
        self.action_card.columnconfigure(0, weight=1)
        self.action_card.columnconfigure(1, weight=1)
        self.action_card.columnconfigure(2, weight=0)
        self.action_card.columnconfigure(3, weight=0)

    def add_action_tab(self):
        action = AddAction(self,1)
        result = action.show()
    
    def load_presets(self):
        action = LoadBox(self,self.actions)
        result = action.show()
        print(result)

if __name__ == "__main__":
    app = App()
    app.mainloop()
