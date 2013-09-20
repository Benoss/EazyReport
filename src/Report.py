from src import model
from libs.db_manager import DBM
from config import Config
import os, csv, datetime
from src.utils import JsonEncoder, Humanize
import time
class ReportInfo(model.ReportInfo):
    
    def create_report(self):
        start_time = time.time()
        if self.source_type == 'SQLquery':
            query_info = model.SQLquery.get(model.SQLquery.id ==  self.source_id)
        connection = model.Connection.get(model.Connection.id ==  query_info.connection_id)
        
        

        filename = os.path.join(Config().cache_folder, self.name + ".csv")
        json_filename = os.path.join(Config().cache_folder, self.name + ".json")
        json_array = []
        with open(filename, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            
            result = DBM(connection.name).query(query_info.sql)
            csv_writer.writerow(result.columns)
            
            for index, row in enumerate(result.rows):
                row = list(row)
                csv_writer.writerow(row)
                json_array.append(row)
        
            self.nb_rows = index + 1
            
        
        
        json_file = open(json_filename, "wb")
        Je = JsonEncoder()
        json_file.write(Je.encode({ "aaData": json_array }))
        self.last_run = datetime.datetime.now()
        self.last_duration = Humanize.pretty_delta(time.time() - start_time)
        self.save()

        
    def create_report_if_needed(self):
        if not self.last_run:
            self.create_report()
        else:
            diff = datetime.datetime.now()- self.last_run
            if diff.seconds > self.cache_duration:
                self.create_report()
        
    def get_header(self):
        filename = os.path.join(Config().cache_folder, self.name + ".csv")
        csvfile = open(filename, 'rb')
        csv_reader = csv.reader(csvfile)
        first_row = csv_reader.next()
        csvfile.close()
        return first_row
    
    def get_rows(self):
        filename = os.path.join(Config().cache_folder, self.name + ".csv")
        csvfile = open(filename, 'rb')
        csv_reader = csv.reader(csvfile)
        return_rows = []
        for line in csv_reader:
            return_rows.append(line)
        return return_rows
        
    def get_json_repr(self):
        return {self.name:
         {
          'last_run':self.last_run,
          'last_duration':self.last_duration,
          'cache_duration':self.cache_duration,
          'report_type':self.report_type,
          'nb_rows':self.nb_rows,
          }
         }
        
        
        
        
        
        
        
        
        
        