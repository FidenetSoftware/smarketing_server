from .sockets_config import connect
from .tw_extraction import get_tweets_by_days, get_tweets_by_date_range

def load_socket_events(sio_server):

    sio_server.on('connect')(connect)

    ##Tw_Extraction table events
    sio_server.on('twitter extractions by days')(get_tweets_by_days)
    sio_server.on('twitter extractions by dates')(get_tweets_by_date_range)
