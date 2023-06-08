from fastapi import WebSocket

class WebsocketManager:
    def __init__(self):
        self.__clients: list[WebSocket] = []
    
    @property
    def clients(self) -> list[WebSocket]:
        return self.__clients
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.__clients.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        await websocket.close()
        self.__clients.remove(websocket)

    async def broadcast(self, data: dict):
        for client in self.__clients:
            await client.send_json(data)