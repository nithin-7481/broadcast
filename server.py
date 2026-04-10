import asyncio
import websockets

clients = set()

async def handler(websocket):
    # Add client
    clients.add(websocket)
    print("Client connected")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            # Broadcast to all clients
            for client in clients:
                if client != websocket:
                    await client.send(message)

    except:
        print("Client disconnected")

    finally:
        clients.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("Server running on ws://localhost:6789")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())