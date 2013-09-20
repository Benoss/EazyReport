from src.utils import singleton, Link, OrderedDict
from src import model
from libs.bottle import abort

def get_path_by_depth(pagepath, depth):
    return "/" +  "/".join(pagepath.strip("/").split("/")[:depth]) + "/"

class MenuItem(model.MenuItem):
    link = None
    
    def is_selected(self, page_path, return_string):
        if page_path in self.get_path():
            return return_string
        else:
            return ""
    
    def get_name(self):
        return self.name
    
    def get_path(self):
        return "/" + self.parent_path.strip("/") + "/" + self.slug_name
  
    def get_parent_path(self):
        return "/" + self.parent_path.strip("/") + "/"
    
    
@singleton
class MenuInfo():
    _menus = None
    
    def get_page(self, page_path):
        if not self._menus:
            self.create_menus()
        
        if not self._menus.has_key(page_path):
            abort(404, "No such database.") 
        return self._menus[page_path]
    
    def get_menu(self, page_path, depth):
        if not self._menus:
            self.create_menus()
        
        if depth == 0:
            raise Exception("Depth 0")
        page_path_deph = get_path_by_depth(page_path, depth)

        return [m for m in self._menus.values() if m.parent_path == page_path_deph]
            
    def reload_menus(self):
        self._menus = None
            
    def create_menus(self):
        if not self._menus:
            self._menus = OrderedDict()
            for menu_item in MenuItem.select().order_by(MenuItem.order.asc()):
                self._menus[menu_item.get_path()] = menu_item
            
