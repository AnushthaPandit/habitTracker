from flask import Flask, request, make_response, redirect, url_for, flash, session
from flask import render_template
from flask_session import Session

from controllers.users import is_valid_creds
from services.users import get_user_details_by_email, insert_user

# creates a Flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hjhjhjTYTYTnjfdsj789'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

def is_logged_in():
	if not session.get("user_id"):
		return False
	else:
		return True
	
def set_login_session(user_id):
	session["user_id"] = user_id;


@app.route("/")
def home():
	message = "Hello, World"
	return render_template('login.html', message=message);

@app.route("/logout")
def logout():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	
	set_login_session(None)
	return redirect(url_for("loginPage"))	

@app.route("/login",  methods=('GET', 'POST'))
def loginPage():
	if is_logged_in():
		return redirect(url_for("dash"))
	
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']
		valid_user_id = is_valid_creds(email,password)
		if(valid_user_id == False):
			flash('Invalid Credentials!')
			return render_template('login.html')
			
		else:
			set_login_session(valid_user_id)
			return redirect(url_for("dash"))
			
	else:
		return render_template('login.html')
	
@app.route("/register",  methods=('GET', 'POST'))
def registerPage():
	if is_logged_in():
		return redirect(url_for("dash"))
	
	if request.method == 'POST':
		email = request.form['email'].strip()
		password = request.form['pass'].strip()
		confirm_pass = request.form['confirmpass'].strip()
		name = request.form['name'].strip()

		if(confirm_pass != password):
			flash("passwords do not matched!")
			return render_template('register.html')

		user = get_user_details_by_email(email)

		if(user != None):
			flash("user with this email already exists!")
			return render_template('register.html')
		
		user_id = insert_user(email, password, name)
		set_login_session(user_id)

		return redirect(url_for("dash"))
			
	else:
		return render_template('register.html')
		

@app.route("/dash")
def dash():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	message = "Hello, World"
	return render_template('dashboard.html', message=message);

@app.route("/compare")
def compare():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	message = "Hello, World"
	return render_template('compare.html', message=message);

@app.route("/progress")
def progress():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	message = "Hello, World"
	return render_template('progress.html', message=message);

@app.route("/tasks")
def tasks():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	message = "Hello, World"
	return render_template('tasks.html', message=message);


# run the application
if __name__ == "__main__":
	app.run(debug=True)
