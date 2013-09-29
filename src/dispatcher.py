from libs import bottle
from libs.bottle import route, template, static_file, post, get
from config import Config
from src.content.menu import MenuInfo
from src import pages
from src.pages import *  # @UnusedWildImport
from src.pages.api_manager import ApiManager

cookie_key = Config().cookie_key


def instantiate_page(page_path):
    menu_item = MenuInfo().get_page(page_path)
    page_module = getattr(pages, menu_item.page_type.lower())
    page_class = getattr(page_module, menu_item.page_type)
    return page_class(page_path, menu_item.page_id)

@route('/favicon.ico')
def facivo():
    return

@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root="./static/")

@route('/cache/<filepath:path>')
def cache_file(filepath):
    return static_file(filepath, root="./cache/")

@route('/')
def default():
    bottle.redirect('/app/home')
    
@post('/login')
@get('/login')
def login_page():
    page = login.Login('login', 1)
    return template('index', page=page)
    
@route('/:module')
@route('/:module/')
def redirect_home(module):
    bottle.redirect("/"+module.rstrip("/") + '/home')     
# 

@post('/api/<pagepath:path>')
@get('/api/<pagepath:path>')
def api(pagepath):
    return ApiManager(pagepath).get_content()


@post('<pagepath:path>')
@get('<pagepath:path>')
def module_subpage(pagepath):
    page=instantiate_page(pagepath)
    if not page.special_return:
        return template('index', page=page)
    else:
        return page.special_return