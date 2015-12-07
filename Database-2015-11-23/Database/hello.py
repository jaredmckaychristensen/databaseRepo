from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from flask import Markup

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '350-databases'
app.config['MYSQL_DATABASE_DB'] = 'marketing'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def hello_world():
    	return render_template('index.html')

@app.route('/employee')
def hello_Tew():
	return render_template('employee.html')

@app.route('/signin', methods=['GET','POST'])
def hello_earth():
	
	#message = Markup("<h1>TEST</h1>")
	#flash(message)
	if request.method == 'POST':
		
		print "here"
        	username_form  = request.form['username']
        	password_form  = request.form['password']
		print username_form,password_form
        	cursor.execute("SELECT * FROM users WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
		print "username exists"
        	if cursor.fetchone()[0]:
			print "made it here"
            		cursor.execute("SELECT password FROM users WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            		for row in cursor.fetchall():
				print "in for loop"
                		#if md5(password_form).hexdigest() == row[0]:
				if password_form == row[0]:
					print "in if"
                    			#session['username'] = request.form['username']
                    			return redirect(url_for('hello_joseph'))
					#return render_template('Managers.html')
                		else:
                    			error = "Invalid Credential"
		else:
            		error = "Invalid Credential"
			print "invalid login"
		print "bad login attempt"
    		return render_template('signin.html', error=error)
	return render_template('signin.html')


@app.route('/managers', methods=['GET', 'POST'])
def hello_joseph():

	if request.method == 'POST':
		if request.form['submit'] == 'Add a Facility':
			print 'you made it past add a facility part'
            		#cursor = db.cursor()
			# execute SQL query using execute() method.
			cursor.execute("INSERT INTO Facilities VALUES(7, 'Alpine-Main', 'Alpine', 'Santa Claus', 65000)")

		elif request.form['submit'] == 'Delete a Facility':
			print 'You made it right before delete'
			cursor.execute('DELETE FROM Facilities WHERE facilityName = "Alpine-Main"') 
			# Fetch a single row using fetchone() method.
			#data = cursor.fetchone()
			print "Success!"
			# disconnect from server
		elif request.form['submit'] == 'Update a Facility':
			cursor.execute('UPDATE Facilities SET facilityManager = "JARED THE BOSS MAN" WHERE facilityCurrentCost > 25000')
		elif request.form['submit'] == 'Sort by Salary':
			cursor.execute('SELECT * FROM Personnel ORDER_BY Salary DESC')
	
	cursor.execute("SELECT * from Facilities")
	data = cursor.fetchall()
	cursor.execute("SELECT * from Personnel")
	personnel = cursor.fetchall()

	return render_template('Managers.html',data=data,personnel=personnel)

if __name__ == '__main__':
    app.run()
