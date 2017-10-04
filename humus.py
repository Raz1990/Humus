from pyquery import PyQuery as pq
import urllib

d = pq(url='https://store.pass.dmm.com/entry/tickets')

f = open('site', 'a+')
f.seek(0)

text = f.read()
print(text)

found = d('div:contains("Suchmos")').html()
print(found)

if (found != text):
    print("WILL NOW WRITE CHANGES INTO site")
    f.write(found)
else:
    print("NO NEW CHANGES")

f.close()
