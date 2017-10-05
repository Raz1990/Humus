from pyquery import PyQuery as pq
import urllib

#path = 'https://store.pass.dmm.com/entry/tickets'

d = pq(url=sys.argv[1])

f = open('site', 'a+')
f.seek(0)

text = f.read()
#print(text)

#search_word = "Suchmos"

found = d('body:contains('+sys.argv[2]+')').text()
#print(found)

if (found != text):
    #print("WILL NOW WRITE CHANGES INTO site")
    f.write(found)
#else:
    #print("NO NEW CHANGES")

f.close()
