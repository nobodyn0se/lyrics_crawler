import bs4 as bs
from googlesearch import search
from urllib.request import Request, urlopen


def get_url(query):
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        return j


def url_parse(url1):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    req = Request(url=url1, headers=hdr)
    wb = urlopen(req).read()
    resp = bs.BeautifulSoup(wb, 'html.parser')
    for para in resp.find_all('div', attrs={'class': 'lyrics'}):
        print(para.text)


def main():
    url = input("What is the name of the song : ")
    query = ''.join([url, "songmeanings.com lyrics"])
    link = get_url(query)
    url_parse(link)


if __name__ == '__main__':
    main()
