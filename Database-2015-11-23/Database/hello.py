from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import Markup

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '350-databases'
app.config['MYSQL_DATABASE_DB'] = 'marketing'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    	return render_template('index.html')

@app.route('/signin', methods=['GET'])
def hello_earth():
		#message = Markup("<h1>TEST</h1>")
	#flash(message)
	return render_template('signin.html')


@app.route('/managers', methods=['GET'])
def hello_joseph():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT * from Marketing")
	data = cursor.fetchall()

	return render_template('Managers.html',data=data)


if __name__ == '__main__':
    app.run()
