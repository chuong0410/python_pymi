import requests
import sys
import json

resp = requests.get("https://api.github.com/users/pymivn/repos")
resp = json.loads(resp.text)
key = sys.argv[1]
def get_repo(user):
	if not user:
		raise SyntaxError("lỗi cú pháp username!")
	resp = requests.get("https://api.github.com/users/{}/repos".format(user))
	if resp.status_code // 100 == 4:
    		raise ValueError("user not found!")
	resp = resp.json()
	list_user = [user['owner']['login'] for user in resp]
	result = []
	for user in resp:
		result.append(user['html_url'])
	return result

def main():
	if len(sys.argv) != 2:
    		raise SyntaxError("Nhập sai cú pháp script : [githubrepos.py] [username]")
	user = sys.argv[1]
	REPOS = get_repo(user)
	print("danh sách các Github respository của user: {} \n".format(user))
	for repos in REPOS:
		print(repos)

if __name__ == "__main__":
	main()