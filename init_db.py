from src.model import StorageDb, User, MenuItem, Connection,\
    ServerConfig, ReportInfo, SQLquery
from src.utils import slugify, random_string
from src.pages.simplepage import SimplePageConfig
    
def create_menu_item(parent_path, name, order, page_type, page_id):
    MenuItem.create(name=name, slug_name=slugify(name), parent_path=parent_path, \
                    order=order, page_type=page_type, page_id=page_id)
    
    
def init_tables():
    StorageDb.connect()
    try:
        User.create_table(True)
        MenuItem.create_table(True)
        SimplePageConfig.create_table(True)
        ReportInfo.create_table(True)
        Connection.create_table(True)
        SQLquery.create_table(True)
        ServerConfig.create_table(True)
        
        User.create(login='test', password='test', name='Test User')
        create_menu_item("/admin/" ,'Home', -1, 'SimplePage', 1)
        SimplePageConfig.create(title="Admin Home", text="This is admin home")
        create_menu_item("/app/" ,'Home', -1, 'SimplePage', 2)
        SimplePageConfig.create(title="Home", text="This is the home page")
        create_menu_item("/admin/" ,'UpdateDB', 0, 'UpdateDB', 3)
        SimplePageConfig.create(title="Menu", text="This is the Menu page")
        create_menu_item("/admin/" ,'Report Creator', 0, 'ReportCreator', 4)
        SimplePageConfig.create(title="Config", text="This is the Config page")
        create_menu_item("/app/" ,'Reports', -1, 'Reports', 5)
        
    
        Connection.create(name="local", description="", connection_engine="mysql", \
                          connection_login="root", connection_password="root", \
                          connection_host ="127.0.0.1", \
                          connection_defaultdb="mysql", connection_port = 3306)
        
        
        
        SQLquery.create(name='test', description='', sql="""SELECT *
                                         FROM mysql.user
                                        """, connection_id=1)
        
        ReportInfo.create(name="Users", description="Report description", source_type='SQLquery', \
                          source_id=1, cache_duration=86000, row_callback=""""fnRowCallback": function( nRow, aData, iDisplayIndex ) {
            $('td:eq(2)', nRow).html('<a href="/testpage?' + aData[2] + '"> link </a>');
            return nRow;
        },""")
        
        ServerConfig.create(key="CookieKey", value=random_string(50))
        ServerConfig.create(key="AppName", value="EazyReport")
        ServerConfig.create(key="CacheFolder", value="cache")
    except Exception, e:
        print "Database already exists", e
    
    