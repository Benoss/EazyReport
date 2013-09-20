import src.model
from libs.db_manager import DBM
from pprint import pprint

class ApiManager():
    def __init__(self, page_path):
        self.page_path = page_path
        self.module = page_path.split("/")[0]
        self.id = int( page_path.split("/")[1])
        self.model_class = getattr(src.model, self.module)
        print self.page_path
        print self.module
        print self.id
        
    def get_content(self):
        pk = [field for field in self.model_class._meta.fields.values() if field.db_field == 'primary_key'][0].name
        print self.id
        report_info = self.model_class.get(getattr(self.model_class, pk) == self.id)
        
        connection = src.model.Connection.get(src.model.Connection.id ==  report_info.connection_id)  # @UndefinedVariable
        result = DBM(connection.name).query(report_info.query)
        pprint([list(row) for row in result.rows])
        pprint(result.columns)
        return {
                "aoColumns" : result.columns,
                "aaData" : [list(row) for row in result.rows]
                }