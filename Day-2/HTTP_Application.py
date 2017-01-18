import http.client

Retrieve = http.client.HTTPConnection("www.github.com")

Retrieve.request("GET", "/index.html")

r1 = Retrieve.getresponse()

print (r1.status, r1.reason)


data1 = r1.read()

Retrieve.request("GET", "/parrot.spam")

r2 = Retrieve.getresponse()

print(r2.status, r2.reason)



data2 = r2.read()

Retrieve.close()
