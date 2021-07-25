import socket
import sys
import random
import os
from INFO import *

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(bytes("PRIVMSG " + "#" + chan + " :" + msg + "\r\n", "UTF-8"))

    def connect(self, server, port, id, chan):
        print("connecting to:" , server)

        self.irc.connect((server, port))
        self.irc.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))                                                         #connects to the SERVER
        self.irc.send(bytes("NICK " + id + "\r\n", "UTF-8"))
        self.irc.send(bytes("JOIN " + "#" + chan + "\r\n", "UTF-8"))

        print("sending: " + "PASS " + "PASS")
        print("sending: " + "NICK " + id)
        print("sending: " + "JOIN " + chan)

    def get_text(self):
        text = self.irc.recv(2040)
        return text

    def pong(self):
        self.irc.send(bytes("PONG " + "%s" + "\r\n" ,"UTF-8"))
        #print("sending: PONG")
