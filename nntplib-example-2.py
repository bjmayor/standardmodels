import nntplib
import string
SERVER = "news.spam.egg"
GROUP  = "comp.lang.python"
KEYWORD = "tkinter"
# connect to server
server = nntplib.NNTP(SERVER)
resp, count, first, last, name = server.group(GROUP)
resp, items = server.xover(first, last)
for id, subject, author, date, message_id, references, size, lines in items:
    if string.find(string.lower(subject), KEYWORD) >= 0:
        resp, id, message_id, text = server.article(id)
        print author
        print subject
        print len(text), "lines in article"