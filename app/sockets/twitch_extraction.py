from ..database import SessionLocal
from ..domain.twitch_extraction import services
from .sockets_config import sio_server

async def get_twitch_extraction_by_days(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        days = data['days']
        result = await services.get_twitch_extractions_by_day(db, id, days)
        await sio_server.emit('twitch extractions by days', {'data': result}, to=sid)
    finally:
        db.close()


async def get_twitch_extraction_by_date_range(sid, data):
   
    db = SessionLocal()
    try:
        id = data['search_id']
        start_date = data['start_date']
        end_date = data['end_date']

        result = await services.get_twitch_extractions_by_date_range(db, id, start_date, end_date)
        await sio_server.emit('twitch extractions by dates', {'data': result}, to=sid)
    finally:
        db.close()