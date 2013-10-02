from src import model
from libs.db_manager import DBM
from config import Config
import os, datetime
from src.utils import JsonEncoder, Humanize
import time


class ChartInfo(model.ChartInfo):
    
    def get_json_path(self):
        return os.path.join(Config().cache_folder, "chart_" + str(self.id) + ".json")
    
    def create_report(self):
        connection = model.Connection.get(model.Connection.id ==  self.connection_id)

        filename = self.get_json_path()
        if self.sql.strip() == '':
            result = DBM(connection.name).quick_query("SELECT 1")
        else:
            result = DBM(connection.name).quick_query(self.sql)
        self.nb_rows = 0
        with open(filename, 'wb') as jsonfile:
            je = JsonEncoder()
            jsonfile.write(je.encode(result))
            
        self.last_run = datetime.datetime.now()
        self.save()

        
    def create_report_if_needed(self):
        if not self.last_run:
            self.create_report()
        else:
            diff = datetime.datetime.now()- self.last_run
            if diff.seconds > self.cache_duration:
                self.create_report()
        
        
    def get_json_repr(self):
        return {self.name:
         {
          'last_run':self.last_run,
          'cache_duration':self.cache_duration,
          'nb_rows':self.nb_rows,
          }
         }
        
        
        
        
        
        
        
        
        
        