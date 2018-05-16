import http.client

conn = http.client.HTTPSConnection("www.regulations.gov")

headers = {
    'cache-control': "no-cache",
    'postman-token': "81936c95-6fc7-ea22-a9be-7abe7c45cab8"
    }

conn.request("GET", "/exportdocket?docketId=BIS-2018-0006", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
