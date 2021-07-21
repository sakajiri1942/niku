import time
import requests
import urllib.request, urllib.error

from bs4 import BeautifulSoup
from numpy import array

#ランキング関係のファイルを出力する

#出力ファイル
out_name = ('C:/xampp/htdocs/niku/部位のランキング.txt')


#入力ファイル　部位のサーチ数を数える
fname = ('C:/xampp/htdocs/niku/元キーワード部位ランキング.txt')
f = open(fname, 'r',encoding='utf-8')
bui_data = f.readlines()
f.close()

brand_count_all = ''
a = 0
for l_data in bui_data:
    time.sleep(1)
    l_data = l_data.replace('\n','')
    a = a + 1

    s_quote = urllib.parse.quote(l_data)
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword=' + s_quote + '&genreId=110428&format=xml'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        # aaaa = 0
        print(l_data, soup.count.text)
        brand_count_all = brand_count_all + l_data+','+str(soup.count.text)+"\n"
    except:
        print('Error')


    if '終わり' in l_data:
        break
    #if a == 2:
    #   break





f = open(out_name, 'w', encoding="utf-8")
f.writelines(brand_count_all)
f.close()

print("ok")
