from src.utils import random_string, slugify
from libs.peewee import SqliteDatabase, MySQLDatabase, Model, CharField,\
    IntegerField, TextField, BooleanField, DateTimeField

import ConfigParser, os




def get_storage_db():
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open('config.ini'))
    except IOError:
        raise Exception("No config file copy config_default.ini to config.ini")
    
    storage_db_type = config.get("General", "storage_db_type")
    if storage_db_type == 'SQLite':
        return SqliteDatabase(config.get("SQLite", "file"))
    elif  storage_db_type == 'MySQL':
        return MySQLDatabase(host=config.get("MySQL", "host"),\
                             user=config.get("MySQL", "login"),\
                             passwd=config.get("MySQL", "password"),\
                             database=config.get("MySQL", "default_db"),\
                             port=config.getint("MySQL", "port"))
        
    


StorageDb = get_storage_db()
class BaseModel(Model):
    class Meta:
        database = StorageDb

class User(BaseModel):
    login = CharField(unique=True)
    password = CharField()
    name = CharField()

class MenuItem(BaseModel):
    name = CharField()
    slug_name = CharField()
    parent_path = CharField()
    order = IntegerField(default=0)
    page_type = CharField()
    page_id = IntegerField()
    
class SQLquery(BaseModel):
    sql = TextField()
    connection_id = IntegerField()
    
    
class ReportInfo(BaseModel):
    name = CharField(unique=True)
    description = TextField(default="")
    cache_duration = IntegerField(default=0)
    last_run = DateTimeField(null=True, default=None)
    last_duration = CharField(null=True, default=None)
    report_type = CharField(default="invisible", index=True)
    nb_rows = IntegerField(default=-1)
    row_callback = TextField(default="")
    source_type = CharField()
    source_id = IntegerField()

    
class Connection(BaseModel):
    name = CharField(unique=True)
    description = TextField()
    connection_engine = CharField()
    connection_host = CharField()
    connection_login = CharField()
    connection_password = CharField()
    connection_defaultdb = CharField()
    connection_port = IntegerField()
    
    
class ServerConfig(BaseModel):
    key = CharField(unique=True)
    value = CharField()
    



    
