from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    	return render_template('index.html')

@app.route('/signin', methods=['GET'])
def hello_earth():
	return render_template('signin.html')

@app.route('/managers', methods=['GET'])
def hello_joseph():
	return render_template('Managers.html')


if __name__ == '__main__':
    app.run()
