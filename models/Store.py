class Store:
    def __init__(self):
        pass

    def save(self,savename,actions,url):
        """Handle the save action and close the dialog."""

        if savename:
            try:
                f = open(f"presets/{savename}.txt","w")
                f.write(url)
                f.write('\n')
                for action in actions:
                    print(action)
                    f.write(str(action))
                    f.write('\n')
                f.close()
            except Exception as e:
                print(e)
            finally:
                return savename

    
    def load(self,filename):
        if filename:
            result = {}
            actions = []
            try:
                with open(f"presets/{filename}.txt", "r") as f:
                    for line in f:
                        action = line.replace('\n',"")
                        actions.append(eval(action))

                result["url"]=actions[0]
                actions.pop(0)
                result["actions"]= actions
                result["name"]= filename
                return result
            except Exception as e:
                print(e)
                return {"error":e}