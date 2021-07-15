import time
import requests
import urllib.request, urllib.error

from bs4 import BeautifulSoup
from numpy import array

fname= ('C:/Users/sakajiri/PycharmProjects/niku/nikuniku-2021-07-15.csv')
f = open(fname, 'r',encoding="cp932")
data = f.readlines()
f.close()

a = 0
for l_data in data:
    #time.sleep(1)
    #l_data = l_data.replace('\n','')
    a = a + 1
    if '全国' not in l_data:
        #print(a, l_data)
        kenbetu_usi = []
        kenbetu_usi = l_data.split(',')

        #県名をはじく 県名は"kenbetu_usi[0]"
        for l_kenbetu_usi in kenbetu_usi:

            if '(' not in l_kenbetu_usi and len(l_kenbetu_usi) > 2:#半角（）
                time.sleep(1)
                l_kenbetu_usi = l_kenbetu_usi.replace('\n', '')
                #print (l_kenbetu_usi)

                s_quote = urllib.parse.quote(l_kenbetu_usi)
                url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword='+s_quote+'&genreId=110428&format=xml'
                #url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1093881737175375236&keyword=%E7%A6%8F%E8%A2%8B&genreId=110428'

                #bs4以外のURL情報取得　あとで削除
                #req = urllib.request.Request(url)
                #with urllib.request.urlopen(req) as res:
                #    body = res.read().decode("utf-8")
                #print(body)

                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html.parser')
                try:
                    #aaaa = 0
                    print(l_kenbetu_usi,soup.count.text)

                except :
                    print('Error')

                #プライスの処理
                #print (soup.find_all('itemPrice'))
                price_moto = soup.find_all('itemprice')
                print(price_moto)
                p = 0                #price_saki = []
                price_all = ''
                for l_price_moto in price_moto:
                    l_price_moto = str(l_price_moto)
                    l_price_moto = l_price_moto.replace('<itemprice>','')
                    l_price_moto = l_price_moto.replace('</itemprice>', '')
                    #print(l_price_moto)
                    #l_price_moto = l_price_moto.replace('\'', '')
                    price_all = price_all+l_price_moto+','


                #print(price_all)
                price_set = []
                price_set = price_all.split(',')
                price_set.remove('')
                price_set_int = list(map(int, price_set))

                price_set_int_sort = sorted(price_set_int, reverse=True)

                moto_kazu = len(price_set_int_sort)
                del_kazu = int(moto_kazu/4)
                if del_kazu > 2:
                    del price_set_int_sort[:del_kazu]
                    price_set_int_sort.pop(-1)
                    #price_set_int_sort.remove('')

                #print(price_set_int_sort)

                souwa = sum(price_set_int_sort)
                kazu = len(price_set_int_sort)

                avg = 0
                if kazu > 1:
                    avg = int(souwa/kazu)
                print(avg,'円')

                #array(aaa)
                #bbb = aaa.replace('<itemprice>','')
                #bbb = bbb.replace('</itemprice>', '')
                #ccc = aaa.split(',')
                #print(aaa)

    if a == 2:
        break
print ("ok")