# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """


    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        self.myClient = client
        self.connection = connection

        # Flag to run thread as a deamon
        self.daemon = True
        self.run()

        # TODO: Finish initialization of MessageReceiver

    def run(self):
        self.myClient.receiveMessage(self.connection.recv())
