from ..database import SessionLocal
from ..domain.tokenization import services
from .sockets_config import sio_server

async def get_results_by_textId(sid, data):

    db = SessionLocal()
    try:
        id = data['text_id']
        result = await services.get_data_by_textId(db, id)
        await sio_server.emit('get tokens', {'data': result}, to=sid)
    finally:
        db.close()