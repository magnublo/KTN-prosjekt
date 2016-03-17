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
            return self.possible_responses[payload['response']](payload)
        else:
            return 'Error. JSON object from server has invalid format.'

    def parse_error(self, message):
        res = message['sender'] + " (error): " + message['content']
        return res

    def parse_info(self, message):
        res = message['sender'] + " (info): " + message['content']
        return res

    def parse_message(self, message):
        res = message['sender'] + " (message): " + message['content']
        return res

    def parse_history(self, message):
        res = ""
        for j in message['content']:
            d = json.loads(j)
            if d['content'] != 'None':
                res += self.parse_message(d)
                res += "\n"

        return res


    # Include more methods for handling the different responses...
