import bs4 as bs
from googlesearch import search
import urllib.request


def get_url(query):
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        return j


def url_parse(url):
    req = urllib.request.urlopen(url).read()
    resp = bs.BeautifulSoup(req, features="lxml")
    for para in resp.find_all('div', attrs={'class': 'holder lyric-box'}):
        print(para.text)


def main():
    url = input("What is the name of the song : ")
    query = ''.join([url, "songmeanings.com lyrics"])
    link = get_url(query)
    url_parse(link)


if __name__ == '__main__':
    main()
