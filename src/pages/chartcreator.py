from src.web_page import WebPage
from src.ChartInfo import ChartInfo
from src.model import SQLquery
from libs.bottle import request, redirect
from src.utils import random_string, Template, Js, Css, JsonEncoder
import pprint
from src.content.highchart import HighChart 

class ChartCreator(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        self.main_template = "chart_creation.tpl"
        self.request_params =  dict(request.params)
        self.chart = None
        self.charts = ChartInfo.select()
        self.table_fields = ChartInfo._meta.fields
        self.action = None
        if  self.request_params.has_key("action"):
            self.action = self.request_params['action']
            if self.action == "create_all":
                json_return = {}
                for chart in self.charts:
                    chart.create_report()
                    json_return.update(chart.get_json_repr())
                Je = JsonEncoder()
                self.special_return = Je.encode(json_return)
            elif self.action == 'new':
                self.chart = ChartInfo.create(name='PlaceHolderName', connection_id=1)
                self.chart.save()
                redirect(self.pagepath + "?chart_id=" + str(self.chart.id) +'&action=edit')
            elif self.request_params.has_key('chart_id'):
                for chart in self.charts:
                    if str(chart.id)==self.request_params['chart_id']:
                        self.chart = chart
            if self.action == 'edit' or self.action == 'new':
                self.chart.create_report_if_needed()
                self.highchart = HighChart(self, self.chart)    
            elif self.action == 'update':
                self.chart.sql = self.request_params['sql']
                self.chart.cache_duration = self.request_params['cache_duration']
                self.chart.name = self.request_params['name']
                self.chart.description = self.request_params['description']
                self.chart.group = self.request_params['group']
                self.chart.save()
                self.chart.create_report()
                redirect(self.pagepath + "?chart_id=" + str(self.chart.id) +'&action=edit' )


    def active(self, page_name):
        if self.chart and page_name == self.chart.name:
            return 'active'
        else:
            return ''



