from libs import bottle
from libs.bottle import run
from src.dispatcher import *
from config import Config
from init_db import init_tables

init_tables()
Config().refresh_config()

#run(host='localhost', port=8090, debug=True)

if __name__ == '__main__':
    try:
        from paste import gzipper  # @UnresolvedImport
        app = gzipper.middleware(bottle.app())
        from cherrypy import wsgiserver  # @UnusedImport @UnresolvedImport

        print "Paste Gzip activated, CherryPy activated"
        run(app=app, host='localhost', port=Config().ServerPort, server='cherrypy')
    except:
        try:
            from cherrypy import wsgiserver  # @UnusedImport @Reimport @UnresolvedImport
            print "Paste Gzip not found, CherryPy activated"
            run(host='localhost', port=Config().ServerPort, server='cherrypy')
        except:
            print "Paste Gzip not found, CherryPy not found Debug mode"
            run(host='localhost', port=Config().ServerPort, debug=True)
