import formatter
import htmllib
w = formatter.DumbWriter() # plain text
f = formatter.AbstractFormatter(w)
file = open("samples/sample.htm")
# print html body as plain text
p = htmllib.HTMLParser(f)
p.feed(file.read())
p.close()
file.close()
# print links print
print
i= 1
for link in p.anchorlist:
    print i, "=>", link
    i=i+ 1