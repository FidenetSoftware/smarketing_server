from ..database import SessionLocal
from ..domain.tw_extraction import service
from .sockets_config import sio_server

async def get_tweets_by_days(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        days = data['days']
        result = await service.get_tweets_by_day(db, id, days)
        await sio_server.emit('twitter extractions by days', {'data': result}, to=sid)
    finally:
        db.close()


async def get_tweets_by_date_range(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        start_date = data['start_date']
        end_date = data['end_date']

        result = await service.get_tweets_by_date_range(db, id, start_date, end_date)
        await sio_server.emit('twitter extractions by dates', {'data': result}, to=sid)
    finally:
        db.close()
