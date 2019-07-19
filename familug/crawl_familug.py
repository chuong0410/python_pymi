import requests
import bs4
import sqlite3
import time
URL_BASE = 'http://www.familug.org/'
DATABASE = 'familug1.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()
c.execute('''CREATE TABLE familug (title text, link_url text, label text)''')
conn.commit()


def crawl_data(label):
    MAGIC_NUMBER = 100000
    ses = requests.Session()
    if label == 'Lastest':
        url = URL_BASE
        pagesize = 10
    else:
        url = "{}search/label/{}".format(URL_BASE, label)
        pagesize = MAGIC_NUMBER
    articles = []
    while True:
        try:
            resp = ses.get(url)
            tree = bs4.BeautifulSoup(resp.text, 'lxml')
            articles.extend(tree.find_all(attrs={'class':
                                                 "post-title entry-title"}))
            if len(articles) > pagesize:
                articles = articles[:10]
                break
            next_page = tree.find('a', attrs={'class': "blog-pager-older-link"}).get('href')
            url = next_page
        except AttributeError:
            break
    for article in articles:
        c.execute('''INSERT INTO familug VALUES
        (?, ?, ?)''', (article.text.strip(), article.a.get('href'), label))
        conn.commit()
        time.sleep(3)
    return


def main():
    labels = ['Lastest', 'Python', 'Command', 'sysadmin']
    for label in labels:
        crawl_data(label)
    conn.close()


if __name__ == "__main__":
    main()
