import os
folders = ["data", "data/logs", "data/userdata"]
for folder in folders:
    try:
        os.mkdir(folder)
    except OSError:
        pass



from MAIN import *

irc = IRC()
f = FUNCTIONS()
text = ""
Loading = True
Main = False
commands = ""

irc.__init__()
irc.connect(SERVER, PORT, BOTID, CHANNEL)


while Loading:
    text = irc.get_text().decode("UTF-8", "ignore")
    print(text)

    if "End of /NAMES list" in text:
        Loading = False
        Main = True
        main(CHANNEL, Main, irc, VIP, f)
