from src.web_page import WebPage
from src.Report import ReportInfo
from libs.bottle import request
from src.utils import random_string, Template, Js, Css
from src.content.datatables import Datatables 

class Login(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        
        self.main_template = "login.tpl"
        self.request_params =  dict(request.params)
        self.error = None