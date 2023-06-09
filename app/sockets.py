import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*'
)
sio_app = socketio.ASGIApp(
    sio_server
)

@sio_server.event
async def connect(sid, environ, auth):
    print(sid, 'connected')
    await sio_server.emit('login', {'join': sid})


