
from flask import Flask
from flask import render_template
from flask import request

import sqlite3
app = Flask(__name__)

DATABASE = '/tmp/example'


def connect_db():
	return sqlite3.connect(DATABASE)

@app.route('/')
def ada_coder():
	conn = connect_db();
	c = conn.cursor()
	c.execute("""select * from cases where completed='FALSE'""")
	info = c.fetchone()
	if(info[1]=='background'):
		info = c.fetchone()
	while(info[2]==''):
		info = c.fetchone()
	conn.close()
	return render_template('layout.html', background=info[1].replace('[ap]',"'"), holding=info[2].replace('[ap]',"'"), caseid=info[0])
	
@app.route('/submit', methods=['POST'])
def submit():
	conn = connect_db()
	c = conn.cursor()
	c = conn.cursor()
	c.execute("""select * from cases where caseid='"""+request.form['caseid']+"'")
	if(c.fetchone()[6]=='TRUE'):
	  return "Data submitted improperly. Please refresh your page."

	command = "update cases "+"set plaintiff='"+request.form['plaintiff']+"', ada='"+request.form["ada"]+"', type='"+request.form["type"]+"', completed='TRUE' where caseid='"+request.form['caseid']+"'"
	c.execute(command)
	conn.commit()
	c.close()
	
	
	return "Thanks for submitting"

if __name__=='__main__':
	app.debug =True
	app.run()

