# ファイルを読み込み、情報にしたがって各県のページを作成する
# PHPもこぴーするので、注意


# 入力ファイル
# C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt


# 出力先
# C:/xampp/htdocs/niku/niku-site/brand_beef

# フォーマット 拡張子がPHPなのは、エディタで編集しやすいため。
# C:/xampp/htdocs/niku/format_ブランド牛各県ページ作成.php
# C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/brand_beef/brand_beef_〇kenmei.php
# 中身：〇県名 > 石川県 　　　　〇本文　＞　PHP等


#CSS の4244行付近　position: relative;　を変えれば画像飛びがなくなる。

# C:/xampp/htdocs/niku/niku-site/inf/ #クーロンで取得したデータを置く場所　実際はサーバー上ローカルはテスト用



burand_f = 'C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt'


f = open(burand_f, 'r', encoding="utf-8")
b_data = f.readlines()
f.close()


format_ken = 'C:/xampp/htdocs/niku/format_ブランド牛各県ページ作成.php'
f = open(format_ken, 'r', encoding="utf-8")
format_data = f.read()
f.close()

copy_moto = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/brand_beef/brand_beef_〇kenmei.php'
f = open(copy_moto, 'r', encoding="utf-8")
cpmoto_data = f.read()
f.close()


outfile_path = 'C:/xampp/htdocs/niku/niku-site/brand_beef/'

#県名等のループ
a = 0
b = 1
format_data2_all = ''
for l_b_data in b_data:
    print(l_b_data)

    #フォーマットファイルの　〇キーワードを書き換え
    ken_inf = l_b_data.split(',')


    #フォーマットをコピーして使用する。各ブランド牛毎
    format_data2 = format_data
    format_data2 = format_data2.replace('〇キーワード',ken_inf[2])

    #県名とブランド牛名を入れる
    cpmoto_data2 = cpmoto_data
    usi_mei = ken_inf[2] +' | ' +ken_inf[0]
    cpmoto_data2 = cpmoto_data2.replace('〇県名', usi_mei)

    #本文は、PHPではなくあらかじめクローンで取得した情報を使用する。
    #cpmoto_data2 = cpmoto_data2.replace('〇本文', format_data2)


    bangou = str(b)
    fname_ken_kobetu = 'brand_beef_' + ken_inf[2] + '_'+ bangou +'.php'
    outfile_path_file_kobetu = outfile_path + fname_ken_kobetu

    f = open(outfile_path_file_kobetu, 'w', encoding="utf-8")
    f.writelines(cpmoto_data2)
    f.close()

    ####
    #県ごとのファイル


    #format_data2_all = format_data2_all + format_data2
    if '終わり' in b_data[a+1]:
        break

    #県ごとのファイル
    ken_inf_tugi = b_data[a+1].split(',')
    if ken_inf[1] not in ken_inf_tugi[1]:
        b = 1
        #ファイルを出力して、特定の情報をリセット？
        cpmoto_data2 = cpmoto_data
        cpmoto_data2 = cpmoto_data2.replace('〇本文',format_data2_all)



        format_data2_all = ''

    #print(format_data2)
    b = b + 1
    a = a + 1
    if a > 23:
        break







