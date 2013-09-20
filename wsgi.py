__author__ = 'benoit'


from libs import bottle
from src.dispatcher import *
from config import Config

from init_db import init_tables
init_tables()
Config().refresh_config()

application = bottle.app()