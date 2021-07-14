
import urllib.request, urllib.error

fname= ('C:/Users/sakajiri/PycharmProjects/niku/ブランド牛の名前.txt')
f = open(fname, 'r',encoding="utf-8")
data = f.readlines()
f.close()


key1 = "item breadcrumb-model breadcrumb -fluid"
key2 = "（"
key3 = "）"
key4 = "件"
key5 = "件）"

gyou_all = ''
for l_data in data:

    #title_data = t_data[1].replace('</h2','')
    l_data = l_data.replace('\n','')
    print(l_data)

    s_quote = urllib.parse.quote(l_data)
    url = 'https://search.rakuten.co.jp/search/mall/'+s_quote+'/110428/?s=3'
    #print (url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
    list_data2 = body.split('\n')
    #print (body)
    for l_data3 in list_data2:
        if key1 in l_data3:
            #kensaku = []
            kensaku_kekka = 0
            if key5 in l_data3:
                kensaku = l_data3.split(key2)
                kensaku2 = kensaku[1].split(key3)
                kensaku_kekka = kensaku2[0].replace(key4,'')
                kensaku_kekka = kensaku_kekka.replace(',', '')
                #print(kensaku_kekka)

            break
    tango_kazu = body.count(l_data)
    if tango_kazu >= 27:
        tango_kazu = str('〇')
    else:
        tango_kazu = str('×')


    print('単語の数',tango_kazu)
    print('商品の数',kensaku_kekka)

    gyou_all = gyou_all+l_data+','+str(tango_kazu)+','+str(kensaku_kekka)+'\n'



fname2= ('C:/Users/sakajiri/PycharmProjects/niku/ブランド牛の名前_数カウント_ランキング用.txt')
f = open(fname2, 'w')
f.writelines(gyou_all)

f.close()
print ('ok')
