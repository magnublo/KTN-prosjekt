# -*- coding: utf-8 -*-
import SocketServer
import datetime
import json

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

messageHistory = []
clientList = []
users = []

def broadcast(jobject):
    for c in clientList:
        c.send_response(jobject)

def getUsers():

    stringWithUsers = ""

    for u in users:
        stringWithUsers += " "
        stringWithUsers += u

    return stringWithUsers

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
        self.username = None
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        clientList.append(self)
        self.bool = True;


        # Loop that listens for messages from the client
        while bool:
            received_string = self.connection.recv(4096)
            self.parseCode(received_string)



    def parseCode(self,json_object):

        dict = json.loads(json_object)

        possible_codes = {
            'login': self.parse_login,
            'logout': self.parse_logout,
            'msg': self.parse_msg,
            'names': self.parse_names,
            'help': self.parse_help
        }

        if dict['request'] in possible_codes:
            possible_codes[dict['request']](dict)
        else:
            self.encode_response('error',"Invalid user request.", 'Server')


    def parse_login(self, dict):

        if not self.validateName(dict['content']):
            self.send_response(self.encode_response('error', "The username is not valid. You can only use characters of a-z or A-Z, or digits( 0-9).",'Server'))

        else:
            self.username = dict['content']
            self.send_response(self.encode_response('info', "Login successful.",'Server'))
            self.send_history()
            users.append(dict['content'])


    def parse_logout(self, dict):
        clientList.remove(self)
        users.remove(self.username)
        self.username = None
        response = self.encode_response('info', "Logout successful.", 'Server')
        self.send_response(response)
        self.bool = False

    def parse_msg(self, dict):
        if self.username != None:
            messageJObject = self.encode_response('message', self.username + ': ' + dict['content'], self.username)
            broadcast(messageJObject)
            messageHistory.append(messageJObject)
        else:
            response = self.encode_response('info', "Login first.", 'Server')
            self.send_response(response)

    def parse_names(self, dict):
        self.send_response(self.encode_response('info', getUsers(), 'Server'))

    def parse_help(self, dict):
        supportedRequests = """Supported requests:
        login <username>, logout, msg <message>, names, help"""
        self.send_response(self.encode_response('info', supportedRequests, 'Server'))

    def send_history(self):
        for j in messageHistory:
            self.send_response(j)

    def validateName(self, name):
        for letter in name:
            if not letter.isalpha() and not letter.isdigit():
                return False

        return True;


    def encode_response(self, response, content, sender):
        time = datetime.datetime.now().time()
        timeString = str(time.hour) + ":" + str(time.minute)
        response = {
            'timestamp': timeString,
            'sender': sender,
            'response': response,
            'content': content
        }

        return json.dumps(response)

    def send_response(self, jobject):
        self.connection.send(jobject)



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
