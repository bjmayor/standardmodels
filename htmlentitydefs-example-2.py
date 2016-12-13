import htmlentitydefs
import re
import cgi
pattern = re.compile("&(\w+?);")
def descape_entity(m, defs=htmlentitydefs.entitydefs):
    # callback: translate one entity to its ISO Latin value
    try:
        return defs[m.group(1)]
    except KeyError:
        return m.group(0) # use as is
def descape(string):
    return pattern.sub(descape_entity, string)
print descape("&lt;spam&amp;eggs&gt;")
print descape(cgi.escape("<spam&eggs>"))