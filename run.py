### chat client proto console edition

from kernel import *
from threading import Thread

irc = IRC()
text = ""
Loading = True
Main = False
commands = ""

irc.__init__()
irc.connect(SERVER, PORT, CLIENTID, CHANNEL)


while Loading:
    text = irc.get_text().decode("UTF-8", "ignore")
    print(text)

    if "End of /NAMES list" in text:
        Loading = False
        Main = True

        Thread(target = receiving(CHANNEL, Main, irc)).start()
        Thread(target = sending(CHANNEL, Main, irc)).start()
