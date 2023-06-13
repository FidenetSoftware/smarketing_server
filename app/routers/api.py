from fastapi import APIRouter

from . import users
from . import search
from . import user_activity
from . import sentiment

from . import tw_extraction

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(users.router)
    router.include_router(search.router)
    router.include_router(user_activity.router)
    router.include_router(sentiment.router)
    router.include_router(tw_extraction.router)
  

include_api_routes()