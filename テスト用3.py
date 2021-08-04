from urllib import request

aaa = request.urlopen('https://www.yahoo.co.jp/')
hhh = aaa.read().decode()
aaa.close()
print(aaa)


#list_data2 = hhh.split('\n')

#print (len(list_data2))