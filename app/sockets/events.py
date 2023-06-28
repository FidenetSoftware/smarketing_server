from .sockets_config import connect
from .tw_extraction import get_tweets_by_days, get_tweets_by_date_range
from .yt_extraction import get_yt_extractions_by_days, get_yt_extractions_by_date_range
from .news_extraction import get_news_extractions_by_days, get_news_extractions_by_date_range
from .twitch_extraction import get_twitch_extraction_by_days, get_twitch_extraction_by_date_range
from .ig_extraction import get_ig_extractions_by_days, get_ig_extractions_by_date_range
from .tokenization import get_results_by_textId

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

    #Twitch_Extraction table events
    sio_server.on('twitch extractions by days')(get_twitch_extraction_by_days)
    sio_server.on('twitch extractions by dates')(get_twitch_extraction_by_date_range)

    #Ig_Extraction table events
    sio_server.on('instagram extractions by days')(get_ig_extractions_by_days)
    sio_server.on('instagram extractions by dates')(get_ig_extractions_by_date_range)
    
    #Tokenization table events
    sio_server.on('get tokens')(get_results_by_textId)