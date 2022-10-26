from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import time
import json
import asyncio
from channels.consumer import SyncConsumer,StopConsumer
class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("connected..")
    
    def receive(self, text_data=None, bytes_data=None):
        for i in range(50):
            self.send(str(i))
            time.sleep(1)
        
        print("message:",text_data)
    def disconnect(self, code):
        print("disconnected...")

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected....")
        print("channel layer.....",self.channel_layer)
        print("channel name......",self.channel_name)
        self.group_name=self.scope["url_route"]["kwargs"]["group_name"]
        print("group name is ",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        #await self.send("message recived from server")

    async def receive(self, text_data=None, bytes_data=None):
        txt_data=json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                'message':txt_data["msg"],
                'user_id':txt_data["user_id"]
            }
        )
        print("message:",text_data)

    async def chat_message(self,event):
        str_dict=json.dumps(event)
        await self.send(str_dict)
        print("event is ",event)


    async def disconnect(self, close_code):
        print("disconnected....")
        await self.close()

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("connected....")
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, text_data=None, bytes_data=None):
        for i in range(50):
            self.send({
            'type':'websocket.send',
            'text':str(i)
            })
            time.sleep(1)
        
        
        print("message:",text_data)
    def websocket_disconnect(self, code):
        print("disconnected...")
        raise StopConsumer()