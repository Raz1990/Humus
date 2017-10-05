from pyquery import PyQuery as pq
import urllib

d = pq(url='https://store.pass.dmm.com/entry/tickets')

#if file doesn't exist, create it. Otherwise, open it for both read/write
f = open('site', 'a+')
#get curser to the beginning, so it could be read from start to end.
f.seek(0)
text = f.read()

#no further use for the file for now
f.close()

print(text)

#search the entire body of the HTML for the keyword
found = d('body:contains('+sys.argv[2]+')').text()
print(found)

if (found != text):
    #print("WILL NOW WRITE CHANGES INTO site")
	#if found new content in HTML, overwrite the existing text file with a new one containing all of the new informtaion
	with open('site','w') as f:
    	f.write(found)
