# SIRIUS が作成したファイルをPHPの実行フォルダに作成する。
# 日本地図バージョン


##########
# ファイル系
# 元ファイル
moto_f = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_brand/index.php'
# 出力ファイル
saki_f = 'C:/xampp/htdocs/niku/niku-site/beef_brand/index.php'
# 必要ファイル
burand_f = 'C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt'
#kenmei_f = 'C:/xampp/htdocs/niku/html_to_県名.txt'

f = open(moto_f, 'r', encoding="utf-8")
m_data = f.readlines()
f.close()

f = open(burand_f, 'r', encoding="utf-8")
b_data = f.readlines()
f.close()

#県名だけを抜き取ったファイルの作成　カウント用
ken_serch_all = ''
for l_b_data in b_data:
    ken_serch = l_b_data.split(',')
    ken_serch_all = ken_serch_all+ken_serch[0]

#print (ken_serch_all)

a = 0
for l_b_data in b_data:
    # print (l_b_data)
    ken1 = l_b_data.split(',')
    ken2 = b_data[a+1].split(',')

    okikae = '<p>' + ken1[0] + '</p>'
    okikae = okikae.replace('\n', '')
    okikae = okikae.replace('県', '')
    okikae = okikae.replace('東京都', '東京')
    okikae = okikae.replace('府', '')
    # 全国の数を変数にいれておく
    zenkoku_kazu = len(b_data) - 1
    #print(okikae)




    #県名カウント
    #次の行の県名といまの行の県名が違ったら実行
    if ken2[0] not in ken1[0]:
        #print (ken1[0],ken2[0])
        ken_kazu = ken_serch_all.count(ken1[0])
        #print (ken_kazu)
        kenmei_roma = ken1[1]
        kenmei_roma = kenmei_roma.replace('\n','')
        #元ファイルの置き換え
        b = 0
        for l_moto_f in m_data:

            if okikae in l_moto_f:


                okikae_ato = '<p>' + ken1[0] +'('+str(ken_kazu)+ ')</p>'
                m_data[b] = m_data[b].replace(okikae, okikae_ato)

                okikae_ken = './beef_brand_' + kenmei_roma + '.php'
                if (b - 2) > 0:

                    #print(kenmei_roma)
                    m_data[b - 2] = m_data[b - 2].replace('#', okikae_ken)
                    #print(m_data[b-2])
                #print(m_data[b])
            b = b + 1



    if '終わり' in b_data[a+1]:
        c = 0
        for l_moto_f in m_data:

            if '現在〇種' in m_data[c]:
                okikae_zentou = '現在'+str(zenkoku_kazu)+'種'
                m_data[c] = m_data[c].replace('現在〇種',okikae_zentou)
                print(m_data[c])
            c = c + 1
        break






    a = a + 1

    #print(len(b_data))

    # break

f = open(saki_f, 'w', encoding="utf-8")
f.writelines(m_data)
f.close()

print("ok")
