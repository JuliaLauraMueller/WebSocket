import websockets
import asyncio
import random
import secrets

class Bot:
    """
    Chat-Bot sending automatic replies to Clients
    """
    def __init__(self, server_ip="$USER", server_port=8080):
        """
        This Chat-Bot binds on defined port and ip "$USER"
        server_ip (str): Either and IPv4 address or a name which can get resolved to an IP address.
        server_port (int): default port is 8080
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.answers = ["Hello user, I am the chat-bot!", "What did you say? Mi mi mi?", 
                        "I'd like to get to know you better", "Don't mess with me and text your colleagues instead"]
    
    async def connection(self):
        """
        Connects the Chat-Bot to the server
        """
        self.websocket = await websockets.connect(f"ws://{self.server_ip}:{self.server_port}")
        print("Connection was successful")
        
        await self.websocket.send("bot") # user 
        while True:
            response = await self.websocket.recv() 
            sender, msg = response.split(':')
            random_item = secrets.choice(self.answers)
            await self.websocket.send(response + f" --> Automatic reply from bot to {sender}: " + random_item)


async def main():
    """
    Creats Bot-Object and executes connection-Method
    """
    bot = Bot(server_ip='kvanc.exercise')
    await bot.connection()
        
if __name__ == "__main__":
    asyncio.run(main())

    
    