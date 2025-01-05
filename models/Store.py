class Save:
    def __init__(self):
        pass

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
            except Exception as e:
                print(e)
            finally:
                self.dialog.destroy()
            # file check
            
        self.result = self.save_name.get()
        self.dialog.destroy()

    def show(self):
        """Show the dialog and wait for user input."""
        self.dialog.wait_window()
        return self.result