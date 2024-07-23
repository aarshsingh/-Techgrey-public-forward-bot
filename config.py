import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "10927702"))
    API_HASH = os.environ.get("API_HASH", "dfd86138a6b2b713cda11ccc926af5c6")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7285200835:AAHMCWBObpUgojmgkAAyXz-nN6c_WKdRK4k")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Ultraforwardme_bot")
    OWNER_ID = os.environ.get("OWNER_ID", "6940013358")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://tgpurpose640:JkxqDWtmLTPtqf43@cluster0.1nlgp9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@Ultrafirwards_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
