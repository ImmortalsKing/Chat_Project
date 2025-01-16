import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from . import models
from .models import Message, UserChannel
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        try:
            user_channel = UserChannel.objects.get(user=self.scope.get('user'))
            user_channel.channel_name = self.channel_name
            user_channel.save()

        except:
            user_channel = UserChannel()
            user_channel.user = self.scope.get('user')
            user_channel.channel_name = self.channel_name
            user_channel.save()

        self.person_id = self.scope.get('url_route').get('kwargs').get('id')

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
        text_data = json.loads(text_data)
        print(text_data.get('type'))
        print(text_data.get('message'))

        other_user = User.objects.get(id=self.person_id)

        new_message = Message()
        new_message.from_who = self.scope.get('user')
        new_message.to_who = User.objects.get(id=self.person_id)
        new_message.message = text_data.get('message')
        new_message.date = '2024-12-15'
        new_message.time = '20:12:10'
        new_message.has_been_seen = False
        new_message.save()

        try:
            user_channel_name = UserChannel.objects.get(user=other_user)
            data = {
                'type': 'receiver_function',
                'type_of_data': 'new_message',
                'data': text_data.get('message')
            }

            async_to_sync(self.channel_layer.send)(user_channel_name.channel_name, data)

        except:
            pass

    def receiver_function(self,data_that_will_come_from_channel):
        data = json.dumps(data_that_will_come_from_channel)
        self.send(data)

