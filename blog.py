#blog.py controller

from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_Key = 'hard_to_guess'

app= Flask(__name__)

app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error = error)

@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', NONE)
	flash('You were logged out')
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)

