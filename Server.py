# -*- coding: utf-8 -*-
import SocketServer
import time
import datetime
import json

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

clientList = []

def broadcast(dict):
    pass
    #Metode skal sende brukernavn og melding til alle i chatrommet.

def listUsers():
    pass
    #Metode skal returnere liste over alle innlogga brukarar.


class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        clientList.add(self)


        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            self.parseCode(received_string)



    def parseCode(self,json_object):

        dict = json.JSON_DECODER(json_object)

        self.possible_codes = {
            'login': self.parse_error(dict),
            'logout': self.parse_info(dict),
            'msg': self.parse_message(dict),
            'names': self.parse_nicknames(dict),
            'help': self.parse_simen(dict)
        }

        if dict['request'] in self.possible_codes:
            return self.possible_codes[dict['request']](dict)
        else:
            return 'Error. JSON object sent from client has invalid format.'



    def login(self,dict):
       self.username = dict['content']

    def logout(self):

    def msg(self):

    def encode_response(self):

        'timestamp' = self.get_timestamp,
        'sender' = self.get_username,
        'response' = self.get_response,
        'content' = self.get_content





    def names(self):

    def help(self):


    def timestamp(string time):
        ts = time.time()

        time  = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
        print time



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """q
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 1337
    print 'Server running...'
    # Set up and initiate the TCP server

    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
