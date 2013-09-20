from src.web_page import WebPage
from src.model import BaseModel
from libs.peewee import CharField


class SimplePageConfig(BaseModel):
    title = CharField()
    text = CharField()

class SimplePage(WebPage):
    def __init__(self, pagepath, page_id):
        WebPage.__init__(self, pagepath)
        page_config = SimplePageConfig.get(id = page_id)
        self.title = page_config.title
        self.text = page_config.text
    
    

        