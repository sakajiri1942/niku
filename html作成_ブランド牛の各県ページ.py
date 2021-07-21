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

php_naiyou = '\n<?php\
$filename = 〇ファイル\
$xml = fopen($filename, \'r\');\
print \'<div class="content_php_afi">\';\
$i = 0;\
foreach($xml->Items->Item as $item){\
  $affiliateUrl = $item->affiliateUrl;\
  $mediumImageUrl = $item->mediumImageUrls->imageUrl;\
  $price = $item->itemPrice;\
  $price2 = number_format( (int)$price );\
  $detail = $item->itemCaption;\
  $detail = mb_substr($detail, 0, 40,"UTF-8") .\'・・・\';\
  $i++;\
  //表示させる数\
  if ( $i > 3 ) {break;}\
  print \'<div class="php_afi_box"><a href="\'.$affiliateUrl.\'" target="_blank"><img src="\'.$mediumImageUrl.\'"></a><br />\'. $detail .\'<br />\'.$price2.\'円\'.\' </div>\'."\n";\
}\
fclose($xml);\
print \'</div>\';\
print \'<!--end/container-->\';\
print \'<br />\';\
?>\
'

#print(php_naiyou)
# CSS の4244行付近　position: relative;　を変えれば画像飛びがなくなる。

# C:/xampp/htdocs/niku/niku-site/inf/ #クーロンで取得したデータを置く場所　実際はサーバー上ローカルはテスト用

harituke_f = 'C:/xampp/htdocs/niku/貼り付け用.php'

f = open(harituke_f, 'r', encoding="utf-8-sig")
h_data = f.read()
f.close()


burand_f = 'C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt'

f = open(burand_f, 'r', encoding="utf-8-sig")
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

# 県名等のループ
a = 0
b = 1
format_data2_all = ''
all_usi = ''
for l_b_data in b_data:
    #print(l_b_data)

    # フォーマットファイルの　〇キーワードを書き換え
    ken_inf = l_b_data.split(',')

    # フォーマットをコピーして使用する。各ブランド牛毎
    format_data2 = format_data
    format_data2 = format_data2.replace('〇キーワード', ken_inf[2])

    # 県名とブランド牛名を入れる
    cpmoto_data2 = cpmoto_data
    usi_mei = ken_inf[2] + ' | ' + ken_inf[0]
    cpmoto_data2 = cpmoto_data2.replace('〇県名', usi_mei)

    # 本文は、PHPではなくあらかじめクローンで取得した情報を使用する。
    # cpmoto_data2 = cpmoto_data2.replace('〇本文', format_data2)

    #PHP貼り付け
    # 別ファイル（貼り付け）のデータ
    #i > 3 )
    okikae_file_name = '../inf/20*' + ken_inf[2] + '.txt'
    h_data2 = h_data
    h_data2 = h_data2.replace('〇ファイル', okikae_file_name)
    h_data2 = h_data2.replace('i > 3', 'i > 30')

    #牛の説明
    usi_setumei = ken_inf[2]+ 'は'+ ken_inf[0]+ken_inf[5]+'で育てられた'+ ken_inf[4]+'です'
    h_data2 = usi_setumei +h_data2
    #PHP貼り付け
    cpmoto_data2 = cpmoto_data2.replace('〇本文', h_data2)

    #bangou = str(b)
    fname_ken_kobetu = 'brand_beef_' + ken_inf[1] + '_' + ken_inf[3] + '.php'
    outfile_path_file_kobetu = outfile_path + fname_ken_kobetu

    f = open(outfile_path_file_kobetu, 'w', encoding="utf-8")
    f.writelines(cpmoto_data2)
    f.close()

    #県ファイルを創るので、行ファイルを変数に隔離
    all_usi = all_usi+':'+l_b_data
    ####
    # 県ごとのファイル

    # format_data2_all = format_data2_all + format_data2
    if '終わり' in b_data[a + 1]:
        break

    # 県ごとのファイル
    naiyou = ''
    ken_inf_tugi = b_data[a + 1].split(',')
    if ken_inf[1] not in ken_inf_tugi[1]:
        b = 1

        #print(all_usi)
        #行から単語にわけていく
        gyou_inf = all_usi.split(':')
        #print(gyou_inf)
        gyou_inf.remove('')
        for l_gyou_inf in gyou_inf:
            #print(l_gyou_inf)
            tango_inf = l_gyou_inf.split(',')
            #print(tango_inf)
            #tango_inf.remove('')
            #print(tango_inf[2])

            naiyou_midasi='<h4>'+tango_inf[2]+'</h4>'
            #print(naiyou)
            #php_naiyou = '<?php
            #$filename = 〇ファイル

            okikae_file_name = '../inf/20*'+tango_inf[2]+'.txt'
            #okikae_file_name = '../inf/2*'+神戸ビーフ.txt'
            #print (okikae_file_name)

            #別ファイル（貼り付け）のデータ
            h_data2 = h_data
            h_data2 = h_data2.replace('〇ファイル',okikae_file_name)


            #もっとみるの作成
            #<h6><a href="####">あああのページへ</a></h6>
            #brand_beef_hokkaidou_hokkaidouohotukuabasiriwagyu
            mottomiru = "<h6><a href=\"./brand_beef_"+tango_inf[1]+"_"+tango_inf[3]+".php\">"+tango_inf[2]+"のページへ</a></h6>"

            naiyou_all = naiyou_all + naiyou_midasi + h_data2 + mottomiru
            #print(naiyou)



        # ファイルを出力して、特定の情報をリセット？
        cpmoto_data2 = cpmoto_data
        cpmoto_data2 = cpmoto_data2.replace('〇本文', naiyou_all)
        cpmoto_data2 = cpmoto_data2.replace('〇県名', tango_inf[0])

        fname_ken_kobetu = 'brand_beef_' + ken_inf[1]  + '.php'
        outfile_path_file_kobetu = outfile_path + fname_ken_kobetu

        f = open(outfile_path_file_kobetu, 'w', encoding="utf-8")
        f.writelines(cpmoto_data2)
        f.close()


        all_usi = ''
    naiyou_all = ''
    # print(format_data2)
    b = b + 1
    a = a + 1
    if a > 23:
        break
