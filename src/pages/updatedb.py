from src.web_page import WebPage
import src.model
from libs.bottle import request, redirect
import pprint

class UpdateDB(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        self.main_template = "update_db.tpl"
        self.request_params =  dict(request.params)
        self.model_list = [ 'ServerConfig', 'MenuItem', 'ReportInfo', 'SQLquery', 'Connection']
        self.rows = None
        self.table_fields_name = []
        self.table_fields_vals = []
        if self.request_params.has_key("table"):
            self.table = self.request_params['table']
            model_class = getattr(src.model, self.table)
            self.table_fields_name = [field[0] for field in model_class._meta.get_sorted_fields()]
            self.table_fields_vals = [field[1] for field in model_class._meta.get_sorted_fields()]
            
            if self.request_params.has_key("action"):
                self.action = self.request_params['action']
                pk = [field for field in self.table_fields_vals if field.db_field == 'primary_key'][0].name
                if self.request_params['action'] == 'edit':
                    self.values = model_class.select().where(getattr(model_class, pk) == self.request_params['id']).dicts()
                elif self.request_params['action'] == 'update':
                    field_to_update = {}
                    for field in self.table_fields_vals:
                        if field.name != pk and field.name in self.request_params.keys():
                            field_to_update[field.name] = self.request_params[field.name]
                    if self.request_params.has_key(pk) and  self.request_params[pk] and self.request_params[pk] != "" and self.request_params[pk] != "AUTO GENERATED":
                        model_class.update(**field_to_update).where(getattr(model_class, pk) == self.request_params[pk]).execute()
                    else:
                        model_class.create(**field_to_update)
                    redirect(self.pagepath + "?table=" + self.table)
            else:
                self.rows = model_class.select().tuples()


        