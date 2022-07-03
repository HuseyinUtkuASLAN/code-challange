import asyncio
import websockets


class Websocket:
    def __init__(self, cache, cacheToHtmlParser):
        self._cache = cache
        self._cacheToHtmlParser = cacheToHtmlParser

    def run(self):
        start_server = websockets.serve(self._handler, "localhost", 8000)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def _handler(self, websocket, path):
        _ = await websocket.recv()
        data_table_text = self._cacheToHtmlParser.parse(self._cache)
        print(data_table_text)
        await websocket.send(data_table_text)
        self._cache.clear()
