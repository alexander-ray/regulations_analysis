import http.client

conn = http.client.HTTPSConnection("www.regulations.gov")

headers = {
    'cache-control': "no-cache"
}

conn.request("GET", "/exportdocket?docketId=BIS-2018-0006", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
