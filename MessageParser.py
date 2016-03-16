import json


class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload['content'])
        else:
            return 'Error. JSON object from server has invalid format.'

    def parse_error(self, message):
        return "Error fra server: " + message

    def parse_info(self, message):
        return "Info fra server: " + message

    def parse_message(self, message):
        return message

    def parse_history(selfself, message):
        pass


    # Include more methods for handling the different responses...
