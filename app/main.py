from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .routers.api import router
from .database import SessionLocal
from .config import API_PREFIX, ALLOWED_HOSTS
from .sockets.sockets_config import sio_app, sio_server
from .sockets.events import load_socket_events
import uvicorn

###
# Main application file
###

def get_application() -> FastAPI:
    ''' Configure, start and return the application '''
    
    ## Start FastApi App 
    application = FastAPI()

    ## Mapping api routes
    application.include_router(router, prefix=API_PREFIX)

    load_socket_events(sio_server)
    application.mount('/ws', sio_app)

    ## Allow cors
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return application


app = get_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    '''
    The middleware we'll add (just a function) will create
    a new SQLAlchemy SessionLocal for each request, add it to
    the request and then close it once the request is finished.
    '''
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)


