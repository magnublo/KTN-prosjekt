# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
from Server import *

class Client():

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        self.host = 'localhost'
        self.server_Port = 1337

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver = None
        self.myParser = MessageParser()

        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        self.connection.connect((self.host, self.server_Port))
        self.receiver = MessageReceiver(self, self.connection)
        self.take_input()
        
    def disconnect(self):
        self.connection.close()

    def receive_message(self, message):
        print(self.myParser.parse(message))

    def send_payload(self, data):
        self.connection.send(data)

    def take_input(self):
        print "Give user input to the chat client."
        userinput = raw_input()
        words = userinput.split(' ', 1)
        if len(words) == 2:
            message_as_dict = {'request': words[0], 'content': words[1]}
        else:
            message_as_dict = {'request': words[0], 'content': None}
        message_as_json = json.dumps(message_as_dict)
        self.send_payload(message_as_json)
        self.take_input()

    def print_text(tekst):
        print("Hei")
# More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 1337)
