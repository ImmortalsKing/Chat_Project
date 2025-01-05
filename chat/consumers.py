from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send("{'type' : 'accept', 'status' : 'accepted'}")

    def receive(self,text_data):
        print(text_data)
        self.send("{'type' : 'event_arrive', 'status' : 'received'}")

    def disconnect(self, code):
        print(code)
        print('Disconnected')
