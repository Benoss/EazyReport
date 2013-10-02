from src.web_page import WebPage
from src.Report import ReportInfo
from libs.bottle import request
from src.utils import random_string, Template, Js, Css
from src.content.highchart import HighChart 

class Chart(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        
        self.main_template = "charts.tpl"
        self.charts = [HighChart(self),HighChart(self),HighChart(self),HighChart(self),HighChart(self)]

    def active(self, page_name):
        return ''

            