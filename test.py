from classes.webdriver import Webdriver


actions = [
    {"function":"click","type":"xpath","path":'/html/body/div[1]/div/div[3]/a[1]/i',"value":"hansaka"},
    {"function":"send_key","type":"xpath","path":'//*[@id="username"]',"value":"hansaka"},
    {"function":"send_key","type":"xpath","path":'//*[@id="password"]',"value":"hansaka"},
    {"function":"click","type":"xpath","path":'//*[@id="login-form"]/div[2]/div[2]/div[1]/form/input',"value":"hansaka"},
    ]

new_drive = Webdriver("http://localhost/galleryCafe/")


for action in actions:
    do_function = action["function"]
    
    if do_function == "click":
        new_drive.on_click(action["type"],action["path"])
        new_drive.onhold(5)
    elif do_function == "send_key":
        new_drive.onhold(4)
        new_drive.assigenValue(action["type"],action["path"],action["value"])
        new_drive.onhold(4)
    else :
        print("error")

