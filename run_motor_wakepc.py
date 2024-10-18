import asyncio
import websockets
import signal

async def websocket_client(uri):
    async with websockets.connect(uri) as websocket:
        print("Connected to the server.")

        # Send an initial message to the server
        await websocket.send("wakepc")
        print("Requesting Motorcontroller to wakepc")

        # Continuously receive messages from the server
        try:
            while True:
                message = await websocket.recv()
                print(f"Received message: {message}")
                # exit condition: check for specific message
                if message == "SUCCESSFUL: Wakepc completed" :
                    print("Successful wakepc. Closing connection.")
                    break
        except websockets.ConnectionClosed:
            print("Connection closed by the server.")
        finally:
            await websocket.close()
            print("Websocket connection closed.")

# Replace 'ws://example.com/socket' with your WebSocket server URI
uri = 'ws://192.168.0.35:8000'

# Run the WebSocket client
asyncio.run(websocket_client(uri))
