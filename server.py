from flask import Flask
from flask import render_template

# creates a Flask application
app = Flask(__name__)


@app.route("/")
def home():
	message = "Hello, World"
	return render_template('login.html', message=message);

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
