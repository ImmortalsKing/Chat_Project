from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

#region comments
        # print(self.scope.get('user').id)
        # print(self.scope.get('session').get('get_me_from_the_consumer'))

        # print(self.channel_layer)
        # print(type(self.channel_layer))

        # print(self.channel_layer.channels)
        # async_to_sync(self.channel_layer.group_add)('MR Chat',self.channel_name)
        # print(self.channel_layer.groups)

    # data = {
    #     'type' : 'receiver_function',
    #     'message' : 'this is MR chatroom',
    #     'website' : 'MR chat'
    # }

    # async_to_sync(self.channel_layer.group_add)('MR_chat',self.channel_name)

    # async_to_sync(self.channel_layer.send)(self.channel_name,data)

    # async_to_sync(self.channel_layer.group_send)('MR_chat',data)
    # async_to_sync(self.channel_layer.group_add)('MR_chat',self.channel_name)

    #endregion

    def receive(self, text_data):
        print(text_data)
        self.send("{'type' : 'event_arrive', 'status' : 'received'}")



    def receiver_function(self,data_that_will_come_from_channel):
        print(data_that_will_come_from_channel)
