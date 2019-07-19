from flask import Flask
from flask import request, jsonify
import json
import sqlite3
import requests
import time

link_url = "https://api.github.com/repos/awesome-jobs/vietnam/issues"
conn = sqlite3.connect('data_job.db')
conn.execute("CREATE TABLE jobs (name text, link text);")
def crawl_data(link_url):
	page = 1
	reps = requests.Session()
	while True:
		params = {'page' : page}
		ses = reps.get(link_url, params = params)
		list_job = ses.json()
		if not list_job:
			break
		for job in list_job:
			conn.execute("INSERT INTO jobs VALUES (?,?)",(job['title'], job['html_url']))
		conn.commit()
		page += 1
		time.sleep(7)
	conn.close()
	return


def main():
	crawl_data(link_url)

if __name__ == "__main__":
	main()