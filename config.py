from libs.db_manager import Stores, DBM
from src.utils import singleton
from src.model import ServerConfig, Connection
from libs.peewee import SqliteDatabase
import os

@singleton
class Config(object):
    ServerPort = 8082
    
    #StorageDb = MySQLDatabase('reportserver', user='root', passwd='root')
    cookie_key = "DefinedLater"
    app_name = "defaultName"
    cache_folder = "cache"
    
    def refresh_config(self):
        self.cookie_key = ServerConfig.get(key="CookieKey").value
        self.cache_folder = ServerConfig.get(key="CacheFolder").value
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)
        for connect in Connection.select():
            Stores().add_store(connect.name, connect.connection_engine, connect.connection_host, connect.connection_login, \
                               connect.connection_password, connect.connection_defaultdb, connect.connection_port)

            #DBM(connect.name).quick_query("SELECT 1")
