
#C:\Users\sakajiri\PycharmProjects\niku\テスト用.text
# <pre>・月日&#009;：&#009;10/21</pre>

harituke_f = 'C:/Users/sakajiri/PycharmProjects/niku/テスト用.text'
f = open(harituke_f, 'r', encoding="utf-8-sig")
b_data = f.readlines()
f.close()

for l_b_data in b_data:
    #print(l_b_data)
    if '    ' in l_b_data:

        l_b_data = l_b_data.replace('   ','&#009;')
        print(l_b_data)