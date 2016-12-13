import urlparse
scheme, host, path, params, query, fragment =\
        urlparse.urlparse("http://host/path;params?query#fragment")
if scheme == "http":
    print "host", "=>", host
    print "path", "=>", urlparse.urlunparse(
    (None, None, path, params, query, None)
    )
