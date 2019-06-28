from IRC import *



def receiving(chan, Main, irc):
    print("FINISHED LOADING")
    print("executing MAIN")

    while Main == True:
        text = irc.get_text()
        text = text.strip(bytes('\r\n', 'UTF-8'))
        text = text.decode('UTF-8', 'ignore')

        buffer = text.replace(':', '')
        user = buffer.split('!', 1)

        user = user[0]

        buffer.replace(buffer, '')
        buffer = text

        data = buffer.replace(':' + user + '!' + user + '@' + user + '.' + 'tmi.twitch.tv ' + 'PRIVMSG ' + '#', '')
        data = data.split(' :', 1)
        data = data[1]

        print(user, ':', data)

        if 'PING :tmi.twitch.tv' == text:
            irc.pong()

def sending(chan, Main, irc):
    while Main == True:
        msg = input()
        irc.send(msg)
