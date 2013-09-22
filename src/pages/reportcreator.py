from src.web_page import WebPage
from src.Report import ReportInfo
from src.model import SQLquery
from libs.bottle import request, redirect
from src.utils import random_string, Template, Js, Css, JsonEncoder
import pprint
from src.content.datatables import Datatables 


class ReportCreator(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        self.report = None
        self.main_template = "report_creation.tpl"
        self.request_params =  dict(request.params)
        
        self.reports = ReportInfo.select()
        self.table_fields = ReportInfo._meta.fields
        self.action = None
        if  self.request_params.has_key("action"):
            self.action = self.request_params['action']
            if self.action == "create_all":
                json_return = {}
                for report in self.reports:
                    report.create_report()
                    json_return.update(report.get_json_repr())
                Je = JsonEncoder()
                self.special_return = Je.encode(json_return)
            elif self.action == 'new':
                self.sql_query = SQLquery.create(sql='select 1', connection_id=1)
                
                self.report = ReportInfo.create(name='PlaceHolderName', description='', source_type='SQLquery', \
                                                source_id=self.sql_query.id)
                
                redirect(self.pagepath + "?report=PlaceHolderName&action=edit" )

            elif self.request_params.has_key('report'):
                self.report = [report for report in self.reports if report.name==self.request_params['report']][0]
                self.sql_query = SQLquery.get(SQLquery.id == self.report.source_id)
            
            if self.action == 'edit' or self.action == 'new':
                self.current_report = self.report
                self.report.create_report_if_needed()
                self.last_run = report.last_run
                self.datatable = Datatables(self, report.name, report.get_header(), report.row_callback)
                
                
#                 
#                 self.header = report.get_header()
#                 self.css.append(Css("DT_bootstrap.css"))
#                 self.foot_js.append(Js("jquery.dataTables.min.js"))
#                 self.foot_js.append(Js("DT_bootstrap.js"))
#                 
#                 self.header = report.get_header()
#                 self.id_table = random_string(10)
#     
#                 self.drop_down_nb = True
#                 self.drop_down_values = [[20, 50, 100, -1], [20, 50, 100, "All"]]
#                 self.drop_down_text = "records per page"
#                 self.global_search = True
#                 self.global_search_text = "Search all columns:"
#                 self.pagination = True
#                 self.show_nb_records = True
#                 self.records_per_page = 20
#                 self.column_search = True
#                 self.foot_js_templates = [Template("datatables_js_ready", self)]
#                 self.ajax_url = "/cache/" + str(report.name) + ".json"
#                 self.csv_url = "/cache/" + str(report.name) + ".csv"
                
                
            elif self.action == 'update':
                self.sql_query.sql = self.request_params['sql_query_sql']
                self.sql_query.save()
                self.report.cache_duration = self.request_params['cache_duration']
                self.report.name = self.request_params['name']
                self.report.description = self.request_params['description']
                self.report.row_callback = self.request_params['row_callback']
                self.report.report_type =  self.request_params['report_type']
                self.report.save()
                self.report.create_report()
                redirect(self.pagepath + "?report=" + self.report.name +'&action=edit' )


    def active(self, page_name):
        if self.report and page_name == self.report.name:
            return 'active'
        else:
            return ''



    def get_type(self, type_name):
        if self.report.report_type == type_name:
            return "selected='selected'"
        else:
            return ""


#     def get_sDom_string(self):
#         return_string = ""
#         ddn = None
#         gs = None
#         pag = None
#         snn = None
#         if self.drop_down_nb:
#             ddn = 'l'
#         if self.global_search:
#             gs = 'f'
#         if ddn or gs:
#             return_string += "<'row'<'col-sm-6'%s><'col-sm-6'%s>r>"%(ddn or '', gs or '')
#         return_string += "t"
#         if self.show_nb_records:
#             pag = "i"
#         if self.pagination:
#             snn = "p"
#         if pag or snn:
#             return_string += "<'row'<'col-sm-6'%s><'col-sm-6'%s>>"%(pag or '', snn or '')
# 
#         return return_string