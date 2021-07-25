
#貼り付け先　テスト
#
harituke_saki = 'C:/xampp/htdocs/niku/niku-site/moto-test.php'
f = open(harituke_saki, 'r', encoding="utf-8-sig")
hs_data = f.read()#ファイルごと読み込む
f.close()


harituke_f = 'C:/xampp/htdocs/niku/貼り付け用.php'
f = open(harituke_f, 'r', encoding="utf-8-sig")
h_data = f.read()#ファイルごと読み込む
f.close()

rank_n = 'C:/xampp/htdocs/niku/元キーワード他肉ランキング.txt'
f = open(rank_n, 'r', encoding="utf-8-sig")
n_data = f.readlines()#一行づつ読み込む
f.close()

rank_b = 'C:/xampp/htdocs/niku/ブランド牛のランキング.csv'
f = open(rank_b, 'r', encoding="utf-8-sig")
r_data = f.readlines()#一行づつ読み込む
f.close()




out_file = 'C:/xampp/htdocs/niku/niku-site/out-test.php'


#ランキング順に並べなおして配列にいれる
nagasa = len(n_data)
rank_n_data = []
for i in range(nagasa):
    kazu = i+1

    #print(kazu)
    for l_n_data in n_data:
        bun = l_n_data.split(',')
        if kazu == int(bun[3]):
            #print (l_n_data)
            rank_n_data.append(l_n_data)

#rank_n_data にランキング順にデータを移動
#print (rank_n_data)

#最終的に張り付ける変数
honbun = ''
a = 0
for l_rank_n_data in rank_n_data:
    bunkatu = l_rank_n_data.split(',')




    #見出し
    a = a + 1
    zyuni = str(a)+'位'

    honbun = honbun+'<h4>'+zyuni+' '+bunkatu[0]+'</h4>'
    harituke_f_cp = harituke_f
    #20210722_ranking_豚肉.txt


    okikaefike = '20*'+bunkatu[0]+'.txt'
    h_data_cp = h_data
    h_data_cp = h_data_cp.replace('〇ファイル', okikaefike)
    #print((okikaefike))
    honbun = honbun + h_data_cp




cpmoto_data2 = hs_data.replace('〇本文',honbun)

f = open(out_file, 'w', encoding="utf-8")
f.writelines(cpmoto_data2)
f.close()


################################################################
#
#ブランド牛ランキング
honbun = ''
a = 0
for l_r_data in r_data:#ブランド牛のランキング順ファイル
    #三重,松阪牛,mie,matusakagyu,6834
    bunkatu = l_r_data.split(',')

    #見出し
    a = a + 1
    zyuni = str(a)+'位'

    honbun = honbun+'<h4>'+zyuni+' '+bunkatu[1]+'</h4>'
    harituke_f_cp = harituke_f
    #


    okikaefike = '20*'+bunkatu[1]+'.txt'
    h_data_cp = h_data
    h_data_cp = h_data_cp.replace('〇ファイル', okikaefike)
    #print((okikaefike))
    honbun = honbun + h_data_cp


    if a == 50:
        break

cpmoto_data2 = hs_data.replace('〇本文',honbun)

f = open(out_file, 'w', encoding="utf-8")
f.writelines(cpmoto_data2)
f.close()
