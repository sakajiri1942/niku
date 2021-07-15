import urllib.request, urllib.error
import os
import time
from datetime import datetime
import datetime
import requests
from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89%E7%89%9B%E4%B8%80%E8%A6%A7"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read().decode("utf-8")
# print (filename2)

# データ検索
# 分析用      URLを配列に
list_data = body.split('\n')
# print(list_data)


# 都道府県の行と最後不要な３行の５０行がある
key01 = "mw-headline"
key02 = "mw-headline\" id=\"関連項目\">関連項目"
key03 = "<a"
key04 = "<h2"
flg1 = 0
# response = request.urlopen(url)
# soup = BeautifulSoup(response)
# response.close()
# print(soup.title)
usi_count = 0
todouhuken = '全国'
gyouall = todouhuken
usi_kazu = 0
zenkoku_usi_kazu = 0
all_inf = ''
z_kazu = ''

# print(datetime.date.today())
for l_data in list_data:

    # 沖縄が検索されて次の１週が必要なので、キーワードは即時終わりではなく次のキーワードになる。
    if key02 in l_data:
        # ループを終了させるついでに数の計算
        z_kazu = '全国(' + str(zenkoku_usi_kazu) + ')'
        break

    if key01 in l_data:
        # 都道府県の名称で真　１週ループさせた後の処理
        # 次の都道府県が真ならば、前の都道府県のデータが確定するということ
        # データが確定してから数や名称の書き込み準備をする
        # すこしややこしくなるが、解りやすいやり方をすると、無駄が非常に多くなる。
        # スタート処理とエンド処理を同時に行うイメージ

        # 都道府県の牛の数。県名で真になるので、カンマの合計をカウントできる。
        usi_kazu = gyouall.count(',')

        # 県内の牛の数を表示させる。県名＋数で置換
        tikan_moto = todouhuken + ','
        tikan_saki = todouhuken + '(' + str(usi_kazu) + '),'
        gyouall = gyouall.replace(tikan_moto, tikan_saki)
        # gyouall = gyouall+todouhuken+','+str(usi_kazu)
        # 全国の牛の数をカウント
        zenkoku_usi_kazu = zenkoku_usi_kazu + usi_kazu
        # print(gyouall)

        # 書き込み用の行データ　行の最後は改行する
        all_inf = all_inf + gyouall + '\n'
        # gyouall = todouhuken

        # 県名がある行で真になるので、確実に県名がl_soupに代入される。
        soup = BeautifulSoup(l_data, "html.parser")  # 一行づつつかう。
        l_soup = soup.text
        # title_data = t_data[1].replace('</h2','')
        # print(todouhuken, usi_count)

        # 県名 我等の
        todouhuken = l_soup.replace('[編集]', '')
        # いたずら系のwikiを修正
        todouhuken = todouhuken.replace('我等の', '')
        gyouall = todouhuken
        flg1 = 1

        usi_count = 0
        # print(l_soup)

    # 牛の名前の検索　wikiの編集の仕方しだいでロジックも変化するかも
    if flg1 == 1 and key03 in l_data and key04 not in l_data:
        soup = BeautifulSoup(l_data, "html.parser")  # 一行づつつかう。
        usi = soup.text
        # 特殊な記述を修正。今後増えることもある
        usi = usi.replace('、', ',')
        usi = usi.replace('[2]', '')
        usi = usi.replace('※三大和牛', '')
        # ()付きの表示を削除
        if '（' in usi:
            usi_bun = usi.split('（')
            usi = usi_bun[0]
        gyouall = gyouall + "," + usi
        usi_count = usi_count + 1

# アウトプットファイル名。日にちでデータを保存。月単位でよいか？
f_name = 'nikuniku-' + str(datetime.date.today()) + '.csv'
print(all_inf)

# 最後のデータで全国の牛の数を置換
all_inf = all_inf.replace('全国', z_kazu)
f = open(f_name, 'w', encoding="cp932")
f.writelines(all_inf)
f.close()

print("ok")
