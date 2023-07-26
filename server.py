from flask import Flask, request, make_response, redirect, url_for, flash
from flask import render_template

from controllers.users import is_valid_creds

# creates a Flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hjhjhjTYTYTnjfdsj789'

@app.route("/")
def home():
	message = "Hello, World"
	return render_template('login.html', message=message);


@app.route("/login",  methods=('GET', 'POST'))
def loginPage():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']
		print(password)
		is_valid = is_valid_creds(email,password)
		if(is_valid == True):
			return redirect(url_for("dash"))
		else:
			flash('Invalid Credentials!')
			return render_template('login.html')
			
	else:
		return render_template('login.html')
	
@app.route("/register",  methods=('GET', 'POST'))
def registerPage():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']
		confirm_pass = request.form['confirmpass']
		name = request.form['name']
		
		print(email)
		print(password)
		print(confirm_pass)
		print(name)

		return render_template('register.html')
			
	else:
		return render_template('register.html')
		

@app.route("/dash")
def dash():
	message = "Hello, World"
	return render_template('dashboard.html', message=message);

@app.route("/compare")
def compare():
	message = "Hello, World"
	return render_template('compare.html', message=message);

@app.route("/progress")
def progress():
	message = "Hello, World"
	return render_template('progress.html', message=message);

@app.route("/tasks")
def tasks():
	message = "Hello, World"
	return render_template('tasks.html', message=message);


# run the application
if __name__ == "__main__":
	app.run(debug=True)
