import asyncio
import websockets
import sys

async def websocket_client(uri):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to the server at {uri}")

        # Send an initial message to the server
        await websocket.send("RUN BATCH SCRIPT")
        print("Requesting to run driversanity.ps1")

        # Continuously receive messages from the server
        try:
            while True:
                message = await websocket.recv()
                print(f"Received message: {message}")
                # exit condition: check for specific message
                if message == "SUCCESSFUL: Wakepc completed":
                    print("Successful wakepc. Closing connection.")
                    break
        except websockets.ConnectionClosed:
            print("Connection closed by the server.")
        finally:
            await websocket.close()
            print("Websocket connection closed.")
            sys.exit(0)

'''
if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        print("{}: '{}'".format(i, arg))

    # Print sys.argv only once
    if len(sys.argv) > 1:
        print(f"sys.argv: {sys.argv[1]}")
'''

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <uri>")
        sys.exit(1)

    uri = sys.argv[1]
    asyncio.run(websocket_client(uri))
