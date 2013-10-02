from src.web_page import WebPage
from src.ChartInfo import ChartInfo
from libs.bottle import request
from src.utils import random_string, Template, Js, Css
from src.content.highchart import HighChart 

class Chart(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        
        self.main_template = "charts.tpl"
        
        self.request_params =  dict(request.params)
        self.all_charts = ChartInfo.select()
        self.chart_groups = set()
        for chart in self.all_charts:
            self.chart_groups.add(chart.group)
        
        self.charts = []
        if self.request_params.has_key('group'):
            for chart in self.all_charts:
                if chart.group == self.request_params['group']:
                    self.charts.append(HighChart(self, chart))
        

    def active(self, page_name):
        return ''

            