from pymongo import MongoClient

import config

Chikudb = MongoClient(config.MONGO_URL)
Chiku = Chikudb["ChikuDb"]["Chiku"]


from .chats import *
from .users import *
