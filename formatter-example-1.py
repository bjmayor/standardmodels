import formatter
import htmllib
w = formatter.AbstractWriter()
f = formatter.AbstractFormatter(w)
file = open("samples/sample.htm")
p = htmllib.HTMLParser(f)
p.feed(file.read())
p.close()
file.close()
