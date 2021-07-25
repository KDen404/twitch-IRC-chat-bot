from IRC import *

user = ""
data = ""

#open("data/commands.txt", "a")
#open("data/quotes.txt", "a")

class FUNCTIONS:
    def reset(self):
        data.replace(data, "")
        user.replace(user, "")


    def addcmd(self, irc, chan, data):
        if len(data.split(" ", 2)) == 3:
            cmd = data.split(" ", 2)
            cmd = cmd[1]

            info = data.split(" ", 2)
            info = info[2]

            c = open("data/commands.txt", "a+")
            c.write("\n" + cmd + ": " + info)
            c.close()

            irc.send(chan, "you succesfully added the command: " + cmd)

            cmd.replace(cmd, "")
            info.replace(info, "")

        else:
            irc.send(chan, "please use this pattern to perform this command: !addcmd [command name] [info]")


    def addQuote(self, irc, chan, data):
        if len(data.split(" ", 1)) == 2:
            info = data.split(" ", 1)
            info = info[1]

            q = open("data/quotes.txt", "a+")
            quotes = q.read().split("\n")

            if info not in quotes:
                q.write("\n" + info)

                irc.send(chan, "Quote has been added succesfully!")
                info.replace(info, "")

                q.close()

            elif info in quotes:

                irc.send(chan,"The Quote has already been added!")
                q.close()


        else:
            irc.send(chan, "please use this pattern to perform this command: !addquote [quote]")


    def chatlog(self, user, data, timestamp):
        log = open("data/logs/log.txt", "a")
        log.write(timestamp +  user + ": " + data + "\n")
