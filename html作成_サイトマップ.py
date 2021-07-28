import glob
from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート


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



bui_f = 'C:/xampp/htdocs/niku/ブランド牛の各ページ情報-追加中（重要）.txt'

f = open(bui_f, 'r', encoding="utf-8-sig")
b_data = f.readlines()
f.close()


copy_moto = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/sitemap.php'
f = open(copy_moto, 'r', encoding="utf-8")
cpmoto_data = f.readlines()
f.close()
#beef_bui_〇bui.php
copy_saki_outfile = 'C:/xampp/htdocs/niku/niku-site/sitemap.php'


copy_moto_kobetu = 'C:/ACES WEB/SIRIUS/サイト生成先/肉のサイト/beef_sonota/beef_sonota_〇niku.php'
f = open(copy_moto_kobetu, 'r', encoding="utf-8")
cpmoto_data_kobetu = f.read()
f.close()


outfile_path = 'C:/xampp/htdocs/niku/niku-site/beef_sonota/index.php'
outfile_path_kobetu = 'C:/xampp/htdocs/niku/niku-site/beef_sonota/'

a = 0
b = 1
format_data2_all = ''
all_usi = ''
naiyou_all = ''


a = 0
file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_brand/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_brand_' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text

   ###県と牛をわける
   if '|' not in bunkatu_japan_moto:
    #print (bunkatu_japan_moto)
    bunkatu_japan = bunkatu_japan_moto.split('|')
    bunkatu2 = bunkatu_japan[0].replace(' ','')
    #print(bunkatu2)

    file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','



a = 0
#file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_brand/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_brand_' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text

   ###県と牛をわける
   if '|' in bunkatu_japan_moto:
    bunkatu_japan = bunkatu_japan_moto.split('|')
    bunkatu2 = bunkatu_japan[0].replace(' ','')
    #print(bunkatu2)

    file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','



#print(file_name)
#print (moto)
#######################
#
#ブランド牛のサイトマップ　PHPファイルを開いて情報を取り出せるが、ファイルで一括に記述する方が安全？
#→PHPファイルから直接ぬきだす。

#print(cpmoto_data)
all_hari = ''
fbunkatu = file_name.split(',')
for l_fbunkatu in fbunkatu:
 #print(l_fbunkatu)
 fbunkatu2 = l_fbunkatu.split(':')
 #print(fbunkatu2[1])
 #rangeエラーを回避する。

 if 'php' in l_fbunkatu:
  #print(fbunkatu2[1])
  #print(fbunkatu2[1])
  if 'のブランド牛' in l_fbunkatu:
   all_hari = all_hari + '<li class="l2"><a href="./beef_brand/'+fbunkatu2[1]+'">'+fbunkatu2[2]+'</a></li>'+"\n"
  else:
   all_hari = all_hari + '<li class="l3"><a href="./beef_brand/' + fbunkatu2[1] + '">' + fbunkatu2[2] + '</a></li>' + "\n"

#print(all_hari)
a = 0
for l_cpmoto_data in cpmoto_data:
 if 'beef_brand/beef_brand_〇kenmei.php' in l_cpmoto_data:
  cpmoto_data[a] = all_hari
  #<li class="l2"><a href="./beef_brand/beef_brand_〇kenmei.php">〇県名のブランド牛</a></li>
 a = a + 1









a = 0
file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_bui/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_bui_' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text
   bunkatu_japan = bunkatu_japan_moto.split('|')
   bunkatu2 = bunkatu_japan[0].replace(' ','')
   #print(bunkatu2)

   file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','
#print(file_name)

all_hari = ''
fbunkatu = file_name.split(',')
for l_fbunkatu in fbunkatu:
 #print(l_fbunkatu)
 fbunkatu2 = l_fbunkatu.split(':')

 if 'php' in l_fbunkatu:
  all_hari = all_hari + '<li class="l2"><a href="./beef_brand/'+fbunkatu2[1]+'">'+fbunkatu2[2]+'</a></li>'+"\n"

a = 0
for l_cpmoto_data in cpmoto_data:
 if 'beef_bui/beef_bui_〇bui.php' in l_cpmoto_data:
  cpmoto_data[a] = all_hari
  #<li class="l2"><a href="./beef_bui/beef_bui_〇bui.php">〇部位</a></li>
 a = a + 1


#################################3
#
#
a = 0
file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_riyou/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_riyou_' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text
   bunkatu_japan = bunkatu_japan_moto.split('|')
   bunkatu2 = bunkatu_japan[0].replace(' ','')
   #print(bunkatu2)

   file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','
#print(file_name)

all_hari = ''
fbunkatu = file_name.split(',')
for l_fbunkatu in fbunkatu:
 #print(l_fbunkatu)
 fbunkatu2 = l_fbunkatu.split(':')

 if 'php' in l_fbunkatu:
  all_hari = all_hari + '<li class="l2"><a href="./beef_riyou/'+fbunkatu2[1]+'">'+fbunkatu2[2]+'</a></li>'+"\n"

a = 0
for l_cpmoto_data in cpmoto_data:
 if 'beef_riyou/beef_riyou_〇riyou.php' in l_cpmoto_data:
  cpmoto_data[a] = all_hari
  #<li class="l2"><a href="./beef_bui/beef_bui_〇bui.php">〇部位</a></li>
 a = a + 1





#################################3
#
#そのた
a = 0
file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_sonota/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_sonota_' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text
   bunkatu_japan = bunkatu_japan_moto.split('|')
   bunkatu2 = bunkatu_japan[0].replace(' ','')
   #print(bunkatu2)

   file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','
#print(file_name)

all_hari = ''
fbunkatu = file_name.split(',')
for l_fbunkatu in fbunkatu:
 #print(l_fbunkatu)
 fbunkatu2 = l_fbunkatu.split(':')

 if 'php' in l_fbunkatu:
  all_hari = all_hari + '<li class="l2"><a href="./beef_sonota/'+fbunkatu2[1]+'">'+fbunkatu2[2]+'</a></li>'+"\n"

a = 0
for l_cpmoto_data in cpmoto_data:
 if 'beef_sonota/beef_sonota_〇niku.php">' in l_cpmoto_data:
  cpmoto_data[a] = all_hari
  #<li class="l2"><a href="./beef_bui/beef_bui_〇bui.php">〇部位</a></li>
 a = a + 1



#################################3
#
#料理
a = 0
file_name = ''
moto = glob.glob('C:/xampp/htdocs/niku/niku-site/beef_ryouri/*')
for l_moto in moto:
  if '.php' in l_moto and 'beef_ryouri' in l_moto:
   bunkatu = l_moto.split('\\')
   #print (bunkatu[1])


   #タイトルを抜き出す。
   f = open(l_moto, 'r', encoding="utf-8")
   cpmoto_data_kobetu = f.read()
   f.close()
   soup = BeautifulSoup(cpmoto_data_kobetu, "html.parser")
   bunkatu_japan_moto = soup.h1.text
   bunkatu_japan = bunkatu_japan_moto.split('|')
   bunkatu2 = bunkatu_japan[0].replace(' ','')
   #print(bunkatu2)

   file_name = file_name + ':'+ bunkatu[1] +':'+ bunkatu2 + ','
#print(file_name)

all_hari = ''
fbunkatu = file_name.split(',')
for l_fbunkatu in fbunkatu:
 #print(l_fbunkatu)
 fbunkatu2 = l_fbunkatu.split(':')

 if 'php' in l_fbunkatu:
  all_hari = all_hari + '<li class="l2"><a href="./beef_ryouri/'+fbunkatu2[1]+'">'+fbunkatu2[2]+'</a></li>'+"\n"

a = 0
for l_cpmoto_data in cpmoto_data:
 if 'beef_ryouri/beef_ryouri_〇ryouri.php">' in l_cpmoto_data:
  cpmoto_data[a] = all_hari
  #<li class="l2"><a href="./beef_bui/beef_bui_〇bui.php">〇部位</a></li>
 a = a + 1



f = open(copy_saki_outfile, 'w', encoding="utf-8")
f.writelines(cpmoto_data)
f.close()
