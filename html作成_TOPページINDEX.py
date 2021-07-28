# ファイルを読み込み、情報にしたがって各県のページを作成する
# PHPもこぴーするので、注意


# 入力ファイル
# C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt


# 出力先
# C:/xampp/htdocs/niku/niku-site/beef_brand

# フォーマット 拡張子がPHPなのは、エディタで編集しやすいため。
# C:/xampp/htdocs/niku/format_ブランド牛各県ページ作成.php
# C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_brand/beef_brand_〇kenmei.php
# 中身：〇県名 > 石川県 　　　　〇本文　＞　PHP等


#print(php_naiyou)
# CSS の4244行付近　position: relative;　を変えれば画像飛びがなくなる。

# C:/xampp/htdocs/niku/niku-site/inf/ #クーロンで取得したデータを置く場所　実際はサーバー上ローカルはテスト用

harituke_f = 'C:/xampp/htdocs/niku/貼り付け用.php'

f = open(harituke_f, 'r', encoding="utf-8-sig")
h_data = f.read()
f.close()

harituke_f = 'C:/xampp/htdocs/niku/貼り付け用日付.php'

f = open(harituke_f, 'r', encoding="utf-8-sig")
hh_data = f.read()
f.close()



bui_f = 'C:/xampp/htdocs/niku/元キーワード他肉ランキング.txt'

f = open(bui_f, 'r', encoding="utf-8-sig")
b_data = f.readlines()
f.close()

burand_f = 'C:/xampp/htdocs/niku/ブランド牛のランキング.csv'

f = open(burand_f, 'r', encoding="utf-8-sig")
brand_data = f.readlines()
f.close()




copy_moto = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/index.php'
f = open(copy_moto, 'r', encoding="utf-8")
cpmoto_data = f.read()
f.close()
#beef_bui_〇bui.php



outfile_path = 'C:/xampp/htdocs/niku/niku-site/index.php'
outfile_path_kobetu = 'C:/xampp/htdocs/niku/niku-site/'

a = 0
b = 1
format_data2_all = ''
all_usi = ''
naiyou_all = ''
for l_brand_data in b_data:

    # PHP貼り付け
    # 別ファイル（貼り付け）のデータ
    # i > 3 )
    # フォーマットファイルの　〇キーワードを書き換え
    bui_inf = l_brand_data.split(',')
    okikae_file_name = 'inf/20*' + bui_inf[0] + '.txt'
    # print(okikae_file_name)
    naiyou_all = naiyou_all + '<h5>' + bui_inf[0] + '</h5>'
    h_data2 = h_data
    h_data2 = h_data2.replace('〇ファイル', okikae_file_name)
    #h_data2 = h_data2.replace('i > 3', 'i > 6')
    naiyou_all = naiyou_all + h_data2
    # naiyou_all = '書き換え'

    #print(l_brand_data)
    a = a + 1
    if a >= 3:
        break

#hh_data
#hh_data 加工
l_hh_data = '<?php'+"\n"+hh_data+"\n"+'?>'
naiyou_all = naiyou_all + '<h6><a href="<% pageDepth %>beef_sonota">その他の肉ページに移動する</a></h6>'
cpmoto_data2 = cpmoto_data
cpmoto_data2 = cpmoto_data2.replace('〇その他の肉', naiyou_all)
cpmoto_data2 = cpmoto_data2.replace('〇時間', l_hh_data)

#print(cpmoto_data2)
f = open(outfile_path, 'w', encoding="utf-8")
f.writelines(cpmoto_data2)
f.close()


