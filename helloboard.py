# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from dbdb import init_db, db_session
from models import User, Article
#from wtforms import Form, TextField, PasswordField, HiddenField, validators

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))

# @app.teardown_request
# def close_db():
#	db_session.remove()

@app.route('/')
def show_entries():
	db_session.commit()
	articles_query = db_session.query(Article)
	entries = [dict(title=article.b_title, body=article.b_body, userid=article.m_id, idx=article.b_idx) for article in articles_query]
	if 'username' in session : print 'User : ' + session['username']

	return render_template('show_entries.html', entries=entries)

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		username =  request.form['username']
		password =  request.form['password']
		if username=='' or password=='':
			error = 'Input something'
		else:
			user = db_session.query(User).filter_by(m_id=username).first()
			if user == None:
				error = 'no such user'
			elif user.m_password != password:
				error = 'password not matched'
			else:
				session['username'] = username
				return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('show_entries'))

@app.route('/<idx>')
def show_entry(idx):
	entry = db_session.query(Article).filter_by(b_idx=idx).first()
	return render_template('show_entry.html', entry=entry)


if __name__ == '__main__':
	init_db()
	app.run(debug=True)





