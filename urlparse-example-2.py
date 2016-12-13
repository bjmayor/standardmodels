import urlparse
scheme, host, path, params, query, fragment = urlparse.urlparse("http://host/path;params?query#fragment")
if scheme == "http":
    print "host", "=>", host
if params:
    path = path + ";" + params
if query:
    path = path + "?" + query
    print "path", "=>", path