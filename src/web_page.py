__author__ = 'benoit'

from src.utils import  Css, Js
from src.content.menu import MenuInfo
from config import Config



class WebPage():
    def __init__(self, pagepath):
        self.pagepath = pagepath
        self.css = [Css("bootstrap.css"), Css("bootstrap_override.css")]
        self.head_js = []
        self.foot_js = [Js("jquery-2.0.0.min.js"), Js("bootstrap.js"),]
        self.foot_js_templates = []
        self.main_template = "simplecontent.tpl"
        self.title = "test"
        self.paragraph = "test"
        self.special_return = None
    
    def get_config(self):
        return Config()
    
    def get_path(self):
        return self.pagepath
    
    def get_menu(self, depth=0):
        return MenuInfo().get_menu(self.pagepath, depth)
    
    def get_foot_js(self):
        output = []
        for x in self.foot_js:
            if x.js_name not in [o.js_name for o in output]:
                output.append(x)
        return output
