import requests
import urllib.request, urllib.error
import time
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

fname= ('C:/Users/sakajiri/PycharmProjects/niku/ブランド牛の名前.txt')
f = open(fname, 'r',encoding="utf-8")
data = f.readlines()
f.close()

for l_data in data:
    time.sleep(1)
    l_data = l_data.replace('\n','')
    #print(l_data)

    s_quote = urllib.parse.quote(l_data)
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword='+s_quote+'&genreId=110428&format=xml'
    #url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword=%E7%A6%8F%E8%A2%8B&genreId=110428'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        print(l_data,soup.count.text)
    except :
        print('Error')