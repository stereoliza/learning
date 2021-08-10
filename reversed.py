import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')
params = urllib.parse.urlencode({
    'access_key': 'f937cc4d1db8c3bff099546054e7ab0d',
    'query': '33.8755584,-118.3121408',
    })
conn.request('GET', '/v1/reverse?{}'.format(params))
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))
