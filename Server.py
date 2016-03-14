# -*- coding: utf-8 -*-
import SocketServer
import time
import datetime

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

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


        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)




    def parseCode(self,json_object):

        if json_object['request'] in self.possible_codes:
            return self.possible_codes[json_object['request']](json_object)
        else:
            return 'Error. JSON object sent from client has invalid format.'

        self.possible_codes = {
            'login': self.parse_error,
            'logout': self.parse_info,
            'msg': self.parse_message,
            'names': self.parse_nicknames,
            'help': self.parse_simen

        }

    def login(self)

        if !ischar(username) || !isdigit(username):
            print ("The username is not valid. You can only use characters of a-z or A-Z, or digits( 0-9).")
            self.parse_error

        else
            print ("Login successful")
            username =

    def logout(self):

    def msg(self):

    def encode_response(self.msg()):
        self.possible_responses = {
        'timestamp' = get_timestamp,
        'sender' = get_username,
        'response' = get_response,
        'content' = get_content

    }



    def names(self):

    def help(self):


    def timestamp(self.encode_response(timestamp())):
        ts = time.time()

        time  = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
        get_timestamp = time

    def sender(self.encode_response(sender()))
        get_username = login.username



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
