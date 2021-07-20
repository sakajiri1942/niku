import time
import requests
import urllib.request, urllib.error

from bs4 import BeautifulSoup
from numpy import array

#出力ファイル
out_name = ('C:/xampp/htdocs/niku/ブランド牛のランキング.txt')

# fname= ('C:/Users/sakajiri/PycharmProjects/niku/nikuniku-2021-07-15.csv')
fname = ('C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt')
f = open(fname, 'r',encoding='utf-8')
data = f.readlines()
f.close()

a = 0
brand_count_all = '';
for l_data in data:
    time.sleep(1)
    # l_data = l_data.replace('\n','')
    a = a + 1
    kenbetu_usi = []
    kenbetu_usi = l_data.split(',')
    #print(kenbetu_usi[2])
    s_quote = urllib.parse.quote(kenbetu_usi[2])
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword=' + s_quote + '&genreId=110428&format=xml'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        # aaaa = 0
        print(kenbetu_usi[2], soup.count.text)
        brand_count_all = brand_count_all + kenbetu_usi[0]+','+ kenbetu_usi[2] + ','+ kenbetu_usi[1]+','+ kenbetu_usi[3] + ','+str(soup.count.text)+"\n"
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
