from src.web_page import WebPage
from src.Report import ReportInfo
from libs.bottle import request
from src.utils import random_string, Template, Js, Css
from src.content.datatables import Datatables 

class Reports(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        
        self.main_template = "reports.tpl"
        self.model_list = []
        self.request_params =  dict(request.params)
        self.current_report = None
        
        self.model_list =  ReportInfo.select().where(ReportInfo.report_type=='report')
        
        for report in self.model_list:
            if self.request_params.has_key("report") and self.request_params["report"] == report.name:
                self.current_report = report
                report.create_report_if_needed()
                self.last_run = report.last_run
                self.datatable = Datatables(self, report.name, report.get_header(), report.row_callback)
                


    def active(self, page_name):
        if self.current_report and page_name == self.current_report.name:
            return 'active'
        else:
            return ''

            