import cherrypy 
import MySQLdb 

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="./salary.py">
          
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

    #@cherrypy.expose


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())





