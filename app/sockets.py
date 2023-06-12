import socketio
from .database import SessionLocal

from .domain.tw_extraction import service

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

@sio_server.on('twitter extractions by days')
async def recive_message(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        days = data['days']
        result = await service.get_tweets_by_day(db, id, days)
        await sio_server.emit('twitter extractions by days', {'data': result}, to=sid)
    finally:
        db.close()
    

@sio_server.on('twitter extractions by dates')
async def recive_message(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        start_date = data['start_date']
        end_date = data['end_date']

        result = await service.get_tweets_by_date_range(db, id, start_date, end_date)
        await sio_server.emit('twitter extractions by dates', {'data': result}, to=sid)
    finally:
        db.close()



# @sio_server.event
# async def disconnect(sid):
#     print('disconnect ', sid)