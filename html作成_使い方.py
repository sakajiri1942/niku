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



bui_f = 'C:/xampp/htdocs/niku/元キーワード検索ブランド牛以外.txt'

f = open(bui_f, 'r', encoding="utf-8-sig")
b_data = f.readlines()
f.close()


copy_moto = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_riyou/index.php'
f = open(copy_moto, 'r', encoding="utf-8")
cpmoto_data = f.read()
f.close()
#beef_bui_〇bui.php

copy_moto_kobetu = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_riyou/beef_riyou_〇riyou.php'
f = open(copy_moto_kobetu, 'r', encoding="utf-8")
cpmoto_data_kobetu = f.read()
f.close()


outfile_path = 'C:/xampp/htdocs/niku/niku-site/beef_riyou/index.php'
outfile_path_kobetu = 'C:/xampp/htdocs/niku/niku-site/beef_riyou/'

a = 0
b = 1
format_data2_all = ''
all_usi = ''
naiyou_all = ''
for l_b_data in b_data:

    if '使い方' in l_b_data:

        # フォーマットファイルの　〇キーワードを書き換え
        bui_inf = l_b_data.split(',')

        naiyou_all = naiyou_all + '<h4>' + bui_inf[0] + '</h4>'


        #PHP貼り付け
        # 別ファイル（貼り付け）のデータ
        #i > 3 )
        okikae_file_name = '../inf/20*' + bui_inf[0] + '.txt'
        #print(okikae_file_name)
        h_data2 = h_data
        h_data2 = h_data2.replace('〇ファイル', okikae_file_name)
        h_data2 = h_data2.replace('i > 3', 'i > 6')
        naiyou_all = naiyou_all + h_data2
        #naiyou_all = '書き換え'
        naiyou_all = naiyou_all + '<h6><a href=./beef_riyou_'+bui_inf[2]+'.php>' + bui_inf[0] + 'の一覧を見る</a></h6>'


        #####
        #
        #個別ファイルの作成
        cpmoto_data_kobetu2 = cpmoto_data_kobetu
        cpmoto_data_kobetu2 = cpmoto_data_kobetu2.replace('〇使い方', bui_inf[0])
        #上記の変数を流用
        h_data2 = h_data2.replace('i > 6', 'i > 30')
        h_data2 = h_data2.replace('//〇日付', hh_data)

        cpmoto_data_kobetu2 = cpmoto_data_kobetu2.replace('〇内容', h_data2)

        outfile_path_kobetu2 = outfile_path_kobetu+'beef_riyou_'+bui_inf[2]+'.php'
        #print (outfile_path_kobetu2)
        f = open(outfile_path_kobetu2, 'w', encoding="utf-8")
        f.writelines(cpmoto_data_kobetu2)
        f.close()

#print(naiyou_all)

#naiyou_all = naiyou_all.replace('<p>', '')
#naiyou_all = naiyou_all.replace('</p>', '')
cpmoto_data2 = cpmoto_data
cpmoto_data2 = cpmoto_data2.replace('〇内容', naiyou_all)

f = open(outfile_path, 'w', encoding="utf-8")
f.writelines(cpmoto_data2)
f.close()




