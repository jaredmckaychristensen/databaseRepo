import cherrypy 
import MySQLdb 


def connect(thread_index): 
    # Create a connection and store it in the current thread 
    cherrypy.thread_data.db = MySQLdb.connect('localhost', 'manager', 'mgrpass', 'marketing') 
    

# Tell CherryPy to call "connect" for each thread, when it starts up 
cherrypy.engine.subscribe('start_thread', connect)

 
class Root: 
    def index(self): 
        # Sample page that displays the number of records in "table" 
        # Open a cursor, using the DB connection for the current thread 
        c = cherrypy.thread_data.db.cursor() 
        c.execute('SELECT * FROM Personnel ORDER BY employeeID DESC') 
        res = c.fetchall()
	result = ""
	for item in res:
		result= result + (str(item)) + "</br>"
        c.close() 
        return "<html><body> %s </body></html>" % result 
    index.exposed = True 
 
cherrypy.quickstart(Root())

