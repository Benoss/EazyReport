from src.utils import random_string, slugify
from libs.peewee import SqliteDatabase, MySQLDatabase, Model, CharField,\
    IntegerField, TextField, BooleanField, DateTimeField

import ConfigParser, os

from _mysql_exceptions import OperationalError


class AutoReconnectMySQLDatabase(MySQLDatabase):
    
    def sql_error_handler(self, exc, sql, params, require_commit):
        if isinstance(exc, OperationalError):
            if exc.errcode in (2006, 2013):
                self.close()
                self.connect()
                return self.execute_sql(sql, params, require_commit)
            
        raise exc
                

def get_storage_db():
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open('config.ini'))
    except IOError:
        raise Exception("No config file copy config_default.ini to config.ini")
    
    storage_db_type = config.get("General", "storage_db_type")
    if storage_db_type == 'SQLite':
        return SqliteDatabase(config.get("SQLite", "file"), threadlocals=True)
    elif  storage_db_type == 'MySQL':
        return AutoReconnectMySQLDatabase(host=config.get("MySQL", "host"),\
                             user=config.get("MySQL", "login"),\
                             passwd=config.get("MySQL", "password"),\
                             database=config.get("MySQL", "default_db"),\
                             port=config.getint("MySQL", "port"), threadlocals=True)
        
    


StorageDb = get_storage_db()
class BaseModel(Model):
    class Meta:
        database = StorageDb

class ChartInfo(BaseModel):
    name = CharField(default='')
    group = CharField(default='')
    description = CharField(default='')
    cache_duration = IntegerField(default=86000)
    last_run = DateTimeField(null=True, default=None)
    sql = TextField(default='')
    connection_id = IntegerField()
    
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
    cache_duration = IntegerField(default=86000)
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
    



    
