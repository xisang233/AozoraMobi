import urllib.request
import bs4
import pickle

def getranking(URL):
    response = urllib.request.urlopen(URL)
    html = response.read()
    bs = bs4.BeautifulSoup(html)
    l = bs.find_all('tr')
    books = []
    for book in l[1:]:
        flag = True
        s = ''
        book = str(book).replace('\u3000', '')
        temp = book[book.index('cards') + 5 : book.index('.html')]
        number = int(temp[temp.index('card') + 4:])
        for c in book:
            if c == '<':
                flag = False
            if flag:
                s += c
            if c == '>':
                flag = True
        s = s.replace('\n\n', '\n')
        message = s.split('\n')[:-1]
        message.append(number)
        message[0] = int(message[0])
        message[3] = int(message[3])
        books.append(message)
    return books

URL_xhtml = 'http://www.aozora.gr.jp/access_ranking/2016_xhtml.html'
URL_txt = 'http://www.aozora.gr.jp/access_ranking/2016_txt.html'

ranking_xhtml = getranking(URL_xhtml)
ranking_txt   = getranking(URL_txt)

with open('ranking_2016.pkl', 'wb') as f:
    pickle.dump((ranking_xhtml, ranking_txt), f)
