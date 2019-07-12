import bs4
import requests
import sys


list_ketqua = ["rs_0_0", "rs_1_0", "rs_2_0", "rs_2_1",
			   "rs_3_0", "rs_3_1", "rs_3_2", "rs_3_3", "rs_3_4", "rs_3_5",
			   "rs_4_0", "rs_4_1", "rs_4_2", "rs_4_3",
			   "rs_5_0", "rs_5_1", "rs_5_2", "rs_5_3", "rs_5_4", "rs_5_5",
			   "rs_6_0", "rs_6_1", "rs_6_2",
			   "rs_7_0", "rs_7_1", "rs_7_2", "rs_7_3"]

class Error(Exception):
	pass

def check_ketqualo(n):
	data = requests.get('http://ketqua.net')
	if data.status_code // 100 == 5:
		raise Error("Cannot connect to server!")
	tree = bs4.BeautifulSoup(data.text)
	date = tree.find(attrs = {'id': "result_date"}).text
	for ketqua in list_ketqua:
		if str(n) == tree.find_all(attrs = {'id': ketqua})[0].text[-2:]:
			if int(ketqua[3]) == 0:
				return "{} bạn đã trúng giải {} với số {}".format(date, "đặc biệt", str(n))
			return "{} bạn đã trúng giải {} với con số {}".format(date, ketqua[3], str(n))
	result = "Rất tiếc bạn không trúng giải nào\nDanh sách giải ngày hôm nay {}:\n".format(date)
	for ketqua in list_ketqua:
    		result += tree.find_all(attrs = {'id': ketqua})[0].text[-2:] + "\n"
	return result

def main():
	if len(sys.argv) != 2:
    		raise SyntaxError("nhập sai cú pháp scripts: [ketqua.y] [num]")
	num = sys.argv[1]
	if len(num) != 2:
		raise ValueError("Nhập lô sai cú pháp: XY")
	print(check_ketqualo(num))


if __name__ == "__main__":
    	main()





