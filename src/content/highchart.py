from src.utils import Js, random_string, Template, JsonEncoder




class HighChart():
    def __init__(self, parent_page, chart_model):
        
        self.parent_page = parent_page
        self.data_json = "/"+chart_model.get_json_path()
        self.parent_page.foot_js.append(Js("highcharts.js"))
        self.parent_page.foot_js.append(Js("highchart_exporting.js"))
        self.template = "highchart.tpl"
        self.id = random_string(10)
        self.width = 400
        self.height = 400
        self.parent_page.foot_js_templates.append(Template("highchart_js.tpl", self))
        
        self.description = chart_model.description
        self.title = chart_model.name
        

    def get_json(self):
        Je = JsonEncoder()
        return Je.encode()
        