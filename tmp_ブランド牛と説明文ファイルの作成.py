# 必要ファイル
burand_f = 'C:/xampp/htdocs/niku/html_to_nikuniku-20217.txt  '  # ブランド牛名がある
kenmei_f = 'C:/xampp/htdocs/niku/html_to_県名.txt'  # ローマ字

# 出力ファイル
saki_f = 'C:/xampp/htdocs/niku/ブランド牛の各ページ情報.txt'

f = open(burand_f, 'r')
b_data = f.readlines()
f.close()

f = open(kenmei_f, 'r', encoding="utf-8")
k_data = f.readlines()
f.close()

gyouall = ''
for l_b_data in b_data:
    # print (l_b_data)
    ken1 = l_b_data.split(',')
    ken2 = ken1[0].split('(')

    okikae = ken2[0].replace('\n', '')
    okikae = okikae.replace('県', '')
    okikae = okikae.replace('東京都', '東京')
    okikae = okikae.replace('府', '')

    # okikae 県名
    # print(okikae)
    a = 0
    for l_k_data in k_data:
        if okikae in l_k_data:
            # print (l_k_data)
            roma = l_k_data.split(',')
            romazi = roma[1]
            romazi = romazi.replace('\n', '')
            # print(romazi)
    gyou = ''
    if '全国' not in l_b_data:
        # ken1 県、牛、牛
        ken1.pop(0)
        # print (ken1)

        gyou = ''
        for l_ken in ken1:
            l_ken = l_ken.replace('\n', '')
            # 個別牛
            # print(l_ken)
            gyou = gyou + ',' + okikae + ',' + romazi + ',' + l_ken + ',' + '\n'
    # b = a.lstrip("AB")
    # gyou = gyou.lstrip(",")
    gyouall = gyouall + gyou
    # print (gyou)
print(gyouall)

f = open(saki_f, 'w', encoding="utf-8")
f.writelines(gyouall)
f.close()
