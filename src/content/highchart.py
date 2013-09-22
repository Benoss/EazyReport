from src.utils import Js, random_string




class HighChart():
    def __init__(self, parent_page):
        parent_page.foot_js.append(Js("highcharts.js"))
        
        self.id = random_string(10)
        self.width = 600
        self.height = 400
        
        