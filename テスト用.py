import urllib.request

url = 'https://www.yahoo.co.jp/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read().decode("utf-8")
#list_data2 = body.split('\n')

print (body)