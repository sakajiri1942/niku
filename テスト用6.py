aaa = '名前,年齢,性別,職業\n\
坂田,22,男,会社員\n\
宮森,31,女,家事手伝\n\
横田,14,女,学生\n\
山岡,52,男,自営業'
bbb = aaa.split('\n')
print(bbb)
for ccc in bbb:
    if '女' in ccc:
        ddd = ccc.split(',')
        print(ddd[0])