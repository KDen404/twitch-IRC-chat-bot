from FUNCTIONS import *
import datetime

def main(chan, Main, irc, VIP, f):
    print("finished Loading")
    print("executing main section")

    while Main:
        text = irc.get_text().strip(bytes("\r\n", "UTF-8")).decode("UTF-8", "ignore")

        buffer = text.replace(":", "")
        user = buffer.split("!", 1)[0]

        buffer.replace(buffer, "")
        buffer = text

        data = buffer.replace(":" + user + "!" + user + "@" + user + "." + "tmi.twitch.tv " + "PRIVMSG " + "#", "").split(" :", 1)[1]

        time = datetime.datetime.now()

        second = str(time.second).strip(" ")
        minute = str(time.minute).strip(" ")
        hour = str(time.hour).strip(" ")

        timestamp = "[" + hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2) + "]"

        f.chatlog(user, data, timestamp)

        print(timestamp, user, ":", data)

        if "PING :tmi.twitch.tv" == text:
            irc.pong()
            f.reset()

        elif data.startswith("!cmdadd"):
            if user in VIP:
                f.addcmd(irc, chan, data)
                f.reset()

            else:
                irc.send(chan, "You don't have the Permissions to perform this command!!")
                f.reset()

        elif data.startswith("!quoteadd"):
            if user in VIP:
                f.addQuote(irc, chan, data)
                f.reset()

            else:
                irc.send(chan, "You don't have the Permissions to perform this command!!")
                irc.reset()

        elif data == "!quote":
            q = open("data/quotes.ccfg", "r")
            quotes = q.read().split("\n")
            quote = random.choice(quotes)

            irc.send(chan, quote)
            print(BOTID + ": " + quote)

            f.reset()
            q.close()

        elif data == "!stop":
            if user == CHANNEL:
                sys.exit(0)
                f.reset()

            else:
                irc.send(chan, "You don't have the permissions to perform this command!!")

        elif data.startswith("!"):
            c = open("data/commands.cfg", "r")
            cr = c.read().split("\n")

            for line in cr:
                cmdline = line.split(": ", 1)
                cmd = cmdline[0]
                info = cmdline[1]

                if data.strip(" ") == cmd:
                    irc.send(chan, info)
                    print(BOTID + ": " + info)

                    cmdline.clear()
                    cmd.replace(cmd, "")
                    info.replace(info, "")

                    f.reset()
                    c.close()
                    break

                else:
                    cmdline.clear()
                    cmd.replace(cmd, "")
                    info.replace(info, "")

        else:
            f.reset()
