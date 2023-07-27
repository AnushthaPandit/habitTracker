from flask import Flask, request, make_response, redirect, url_for, flash, session
from flask import render_template
from flask_session import Session

from controllers.users import is_valid_creds
from services.users import get_user_details_by_email, insert_user
from services.habits import insert_habit, get_habits_by_user_id, delete_habit_by_id

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

def get_login_session():
	return session["user_id"]


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
	
	tasks = get_habits_by_user_id(int(get_login_session()))
	return render_template('tasks.html', tasks=tasks);

@app.route("/add-new-task",  methods=('POST',))
def addNewTask():
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	
	if request.method == 'POST':
		title = request.form['title'].strip()
		duration = request.form['duration'].strip()

		insert_habit(title, int(duration), int(get_login_session()))
		return redirect(url_for("tasks"))
			
	else:
		return redirect(url_for("tasks"))
	
@app.route("/delete-task/<int:habit_id>")
def deleteTask(habit_id):
	if not is_logged_in():
		return redirect(url_for("loginPage"))
	
	
	delete_habit_by_id(habit_id)
	return redirect(url_for("tasks"))
			


# run the application
if __name__ == "__main__":
	app.run(debug=True)
