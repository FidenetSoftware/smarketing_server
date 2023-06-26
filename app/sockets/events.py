from .sockets_config import connect
from .tw_extraction import get_tweets_by_days, get_tweets_by_date_range
from .yt_extraction import get_yt_extractions_by_days, get_yt_extractions_by_date_range
from .news_extraction import get_news_extractions_by_days, get_news_extractions_by_date_range


def load_socket_events(sio_server):

    sio_server.on('connect')(connect)

    #Yt_Extraction table events
    sio_server.on('youtube extractions by days')(get_yt_extractions_by_days)
    sio_server.on('youtube extractions by dates')(get_yt_extractions_by_date_range)

    #Tw_Extraction table events
    sio_server.on('twitter extractions by days')(get_tweets_by_days)
    sio_server.on('twitter extractions by dates')(get_tweets_by_date_range)

    #News_Extraction table events
    sio_server.on('news extractions by days')(get_news_extractions_by_days)
    sio_server.on('news extractions by dates')(get_news_extractions_by_date_range)
