from flask import Flask
from flask import request, jsonify
import json
import sqlite3


conn = sqlite3.connect("data_job.db", check_same_thread=False)
conn.commit()
data = conn.execute('SELECT * FROM jobs;')
app = Flask(__name__)
@app.route("/")
def begin():
	result = "<hr><h1>Tuyển dụng IT Việt Nam :</h1><hr><ul><br>"
	lines = []
	for name, link in data.fetchall():
		line = "<h3><li>{} ----> <a href={}> {}</a> {}</li></h3>".format(name, link, link, "<br>")
		lines.append(line)
	result += "<br>".join(lines) + "</ul>"
	return result

if __name__ == "__main__":
	app.run(debug = True)