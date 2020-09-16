import json
from channels.generic.websocket import WebsocketConsumer
from .views import publisAutcompletion

class AutocompletionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        message = text_data_json['message']#We load the value in the input
        print("The message is  ######  : " + message)
        publications = publisAutcompletion(message) #We search for the publications matching the query
        self.send(text_data=json.dumps({
            'message': publications
        }))