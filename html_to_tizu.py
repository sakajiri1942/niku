# SIRIUS が作成したファイルをPHPの実行フォルダに作成する。
# 日本地図バージョン


##########
# ファイル系
# 元ファイル
moto_f = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_brand/index.php'
# 出力ファイル
saki_f = 'C:/xampp/htdocs/niku/niku-site/beef_brand/index.php'
# 必要ファイル
burand_f = 'C:/xampp/htdocs/niku/html_to_nikuniku-20217.txt'
kenmei_f = 'C:/xampp/htdocs/niku/html_to_県名.txt'

f = open(moto_f, 'r', encoding="utf-8")
data = f.readlines()
f.close()

f = open(burand_f, 'r')
b_data = f.readlines()
f.close()

f = open(kenmei_f, 'r', encoding="utf-8")
k_data = f.readlines()
f.close()

for l_b_data in b_data:
    # print (l_b_data)
    ken1 = l_b_data.split(',')
    ken2 = ken1[0].split('(')

    okikae = '<p>' + ken1[0] + ')</p>'
    okikae = okikae.replace('\n', '')
    okikae = okikae.replace('県', '')
    okikae = okikae.replace('東京都', '東京')
    okikae = okikae.replace('府', '')
    # 全国の数を変数にいれておく
    if '全国' in l_b_data:
        zenkoku_kazu = ken2[1]

    # 県名をとりだす
    kenmei = ken2[0].replace('県', '')
    kenmei = kenmei.replace('東京都', '東京')
    kenmei = kenmei.replace('府', '')

    # ヒット数を１にするために、両方に<p>をつけておく。
    kenmei = '<p>' + kenmei + '</p>'
    # print(kenmei)

    # HTML　のファイルを書き換える
    a = 0
    for l_data in data:
        if kenmei in l_data:
            # print (kenmei)
            henkan_moto = l_data
            henkan_moto = henkan_moto.replace('\n', '')
            data[a] = data[a].replace(henkan_moto, okikae)
            # print( data[a])
            break
        # print(a)
        # if l_data
        a = a + 1

    # break

# 全国の頭数をいれる
# zenkoku_kazu
a = 0
for l_data in data:
    if '〇種' in l_data:
        zenkoku_kazu = '<strong>' + zenkoku_kazu + '</strong>'
        zenkoku_kazu = zenkoku_kazu.replace('\n', '')
        data[a] = data[a].replace('〇', zenkoku_kazu)
        break
    a = a + 1

##########
# リンクを挿入
for l_k_data in k_data:
    # print (l_b_data)
    ken1 = l_k_data.split(',')
    kenmei_nihon = ken1[0].replace('\n', '')
    kenmei_roma = ken1[1].replace('\n', '')

    # 元のデータの書き換えループ
    a = 0
    for l_data in data:
        if kenmei_nihon in l_data and 'class' not in l_data:

            # 置き換えローマ字
            okikae_ken = 'beef_brand_' + kenmei_roma + '.php'
            if (a - 2) > 0:
                print(kenmei_roma)
                data[a - 2] = data[a - 2].replace('#', okikae_ken)

        a = a + 1

f = open(saki_f, 'w', encoding="utf-8")
f.writelines(data)
f.close()

print("ok")
