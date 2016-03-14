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
        payload = json.JSONDecoder(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return 'Error. JSON object from server has invalid format.'

    def parse_error(self, payload):
        return "Error fra server: " + payload.split()[2]

    def parse_info(self, payload):
        return "Info fra server: " + payload.split()[2]

    def parse_message(self, payload):
        return payload.split()[2]

    def parse_history(selfself, payload):
        pass


    # Include more methods for handling the different responses...
