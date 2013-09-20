from src.utils import random_string, Template, Js, Css, slugify

class Datatables():
    def __init__(self, parent_page, name, headers, row_callback=""):
        self.parent_page = parent_page
        self.parent_page.css.append(Css("DT_bootstrap.css"))
        self.parent_page.foot_js.append(Js("jquery.dataTables.min.js"))
        self.parent_page.foot_js.append(Js("DT_bootstrap.js"))
        self.parent_page.foot_js_templates = [Template("datatables_js_ready", self)]
        
        self.template = "datatables.tpl"
        self.row_callback = row_callback
        self.id_table = random_string(10)
        self.header = headers
        self.drop_down_nb = True
        self.drop_down_values = [[20, 50, 100, -1], [20, 50, 100, "All"]]
        self.drop_down_text = "records per page"
        self.global_search = True
        self.global_search_text = "Search all columns:"
        self.pagination = True
        self.show_nb_records = True
        self.records_per_page = 20
        self.column_search = True

        self.ajax_url = "/cache/" + str(name) + ".json"
        self.csv_url = "/cache/" + str(name) + ".csv"
        
        
    def get_sDom_string(self):
        return_string = ""
        ddn = None
        gs = None
        pag = None
        snn = None
        if self.drop_down_nb:
            ddn = 'l'
        if self.global_search:
            gs = 'f'
        if ddn or gs:
            return_string += "<'row'<'col-sm-6'%s><'col-sm-6'%s>r>"%(ddn or '', gs or '')
        return_string += "t"
        if self.show_nb_records:
            pag = "i"
        if self.pagination:
            snn = "p"
        if pag or snn:
            return_string += "<'row'<'col-sm-6'%s><'col-sm-6'%s>>"%(pag or '', snn or '')

        return return_string
    
    def slugify(self, input_string):
        return slugify(input_string)