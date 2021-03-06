import asyncio


# predefined events
EVT_READY = "gameReady"
EVT_ERROR = "wsError"


# Client class represents a game client connected over ws
class Client:

    def __init__(self, ws):
        self.ws = ws
        self.done = asyncio.Event()

    async def notify(self, event, data=None):
        await self.ws.send_json({"event": event, "data": data or {}})

    # wait until a client has finished playing
    async def wait_finished(self):
        await self.done.wait()

    # set client's state to finished
    def set_finished(self):
        self.done.set()
