import asyncio
import websockets

async def chat():
    uri = "ws://localhost:6789"

    async with websockets.connect(uri) as websocket:
        print("Connected to server")

        async def send():
            while True:
                msg = input("You: ")
                await websocket.send(msg)

        async def receive():
            while True:
                msg = await websocket.recv()
                print(f"Received: {msg}")

        await asyncio.gather(send(), receive())


asyncio.run(chat())