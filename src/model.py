from src.utils import random_string, slugify
from libs.peewee import SqliteDatabase, MySQLDatabase, Model, CharField,\
    IntegerField, TextField, BooleanField, DateTimeField

StorageDb = SqliteDatabase('reportserver.db')
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
    



    
