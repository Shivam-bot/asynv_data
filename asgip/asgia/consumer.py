from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import asyncio
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TestConsumer(WebsocketConsumer):

    def connect(self):
        # print(self.scope, "scope")
        print('in connection New')
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(
             self.room_group_name,self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({'status':"Connected"}))

    def receive(self,text_data):
        print('data_received New', text_data)

        # print(self.scope, "receive")
        # print(json.loads(text_data), "receive")
        asd = text_data
        if asd == text_data:
            self.disconnect()
        self.send(text_data=json.dumps({'status':"get data"}))

    def disconnect(self, *args, **kwargs):
        print('diconnected NEw')

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        print(data,'not. foundhhbbhhb')
        self.send(text_data=json.dumps({"payloads":data}))


class NewConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = 'new_consumer'
        self.room_group_name = 'new_consumer_group'
        await(self.channel_layer.group_add)(
             self.room_group_name,self.channel_name
        )
        await self.accept()
        await self.send(text_data = json.dumps({'status':"Connected to new async json consumer"}))

    async def receive(self,text_data):
        await self.send(text_data = json.dumps({'status':"get data for new consumer"}))
    
    async def disconnect(self, *args, **kwargs):
        await self.send(text_data =json.dumps({'status': 'disconnected'}))


    async def send_notification(self, event):
            print(event)
            data = json.loads(event.get('value'))
            await self.send(text_data = json.dumps({"payloads":data}))