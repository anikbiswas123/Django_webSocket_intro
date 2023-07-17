

# topics - websocket Api - javascripts 

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from time import sleep


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Connect...........")
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("Receive...........")
        print("Message is: ", event['text'])
        
        for i in range(50):
           self.send({
                "type": "websocket.send",
                "text":str(i),
            })
           sleep(1)
            


     
      
    
    def websocket_disconnect(self, event):
        print("Disconnect...........")
        raise StopConsumer()
        
        

class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, message):
        print("connect.........")
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, message):
        print("Receive...........")
        print("Message is: ", message['text'])
        
        # await asyncio.sleep(1)
        for i in range(50):
             await self.send({
            "type": "websocket.send",
            "text": str(i),
        })
        sleep(1)
       
            
    async def websocket_disconnect(self,event):
        print("Websocket disconnect.....",event)
        raise StopConsumer                  