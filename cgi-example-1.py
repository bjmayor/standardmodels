import cgi
import os, urllib
ROOT = "samples"
# header

print "text/html"
print
query = os.environ.get("QUERY_STRING")
if not query:
    query = "."
script = os.environ.get("SCRIPT_NAME", "")
if not script:
    script = "cgi-example-1.py"
print "<html>"
print "<head>"
print "<title>file listing</title>"
print "</head>"
print "</html>"
print "<body>"
try:
    files = os.listdir(os.path.join(ROOT, query))
except os.error:
    files = []
for file in files:
    link = cgi.escape(file)
    if os.path.isdir(os.path.join(ROOT, query, file)):
        href = script + "?" + os.path.join(query, file)
        print "<p><a href= '%s'>%s</a>" % (href, cgi.escape(link))
    else:
        print "<p>%s" % link
print "</body>"
print "</html>"