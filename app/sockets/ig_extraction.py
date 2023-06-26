from ..database import SessionLocal
from ..domain.ig_extraction import services
from .sockets_config import sio_server


async def get_ig_extractions_by_days(sid, data):
   
    db = SessionLocal()
    try:
        string = data['string']
        days = data['days']
        result = await services.get_ig_extraction_by_day(db, string, days)
        await sio_server.emit('instagram extractions by days', {'data': result}, to=sid)
    finally:
        db.close()


async def get_ig_extractions_by_date_range(sid, data):
   
    db = SessionLocal()
    try:
        string = data['string']
        start_date = data['start_date']
        end_date = data['end_date']

        result = await services.get_ig_extraction_by_date_range(db, string, start_date, end_date)
        await sio_server.emit('instagram extractions by dates', {'data': result}, to=sid)
    finally:
        db.close()