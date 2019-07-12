import bs4
import requests
import sys
import json

N, LABEL = sys.argv[1], sys.argv[2]
link_url = "https://api.stackexchange.com/2.2/questions"

optimine = {'pagesize': N,
			'order' : 'desc',
			'sort': 'votes',
			'tagged': LABEL,
			'site': 'stackoverflow'}


def get_question(N, LABEL):
	ses = requests.Session()
	resp = ses.get(link_url, params = optimine)
	resp = resp.json()
	tags = []

	if not resp['items']:
    		raise ValueError("Data not found!")
	for tag in resp['items']:
		tags.extend(tag['tags'])
	result = []
	top_question = []
	for value in resp['items']:
		if LABEL in value['tags']:
			result.append((value['title'],value['link']))
	for question in result[:int(N)]:
		top_question.append(question)
	return top_question


def main():
	if len(sys.argv) != 3:
		raise TypeError("sai cú pháp script : [so.py] [N] [LABEL]")
	N = sys.argv[1]
	LABEL = sys.argv[2]
	print("Top {} câu hỏi liên quan đến {} :".format(N, LABEL))
	for question in get_question(N, LABEL):
    		print(question)

if __name__ == "__main__":
    	main()







