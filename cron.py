import os
from libs import bottle
from libs.bottle import run
from src.dispatcher import *
from config import Config
from init_db import init_tables
from src.Report import ReportInfo 

Config().refresh_config()

reports = ReportInfo.select()


json_return = {}
for report in reports:
    report.create_report()
    json_return.update(report.get_json_repr())


print json_return