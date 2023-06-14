import socketio
from ..database import SessionLocal
from ..domain.tw_extraction import service


sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='https://smartketing-29bx.onrender.com'
)

sio_app = socketio.ASGIApp(
    sio_server
)

@sio_server.event
async def connect(sid, environ, auth):
    print(sid, 'connected')
    await sio_server.emit('login', {'join': sid})



    



