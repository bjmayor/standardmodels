class HTTPError(Exception):
    # indicates an HTTP protocol error
    def __init__(self, url, errcode, errmsg):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return ( "<HTTPError for %s: %s %s>"
        %  (self.url,
        self.errcode,  self.errmsg)
        )

try:
    raise HTTPError("http://www.python.org/foo", 200, "Not Found")
except HTTPError, error:
    print "url", "= >", error.url
    print "errcode", "=>", error.errcode
    print "errmsg", "= >", error.errmsg

    raise # reraise  exception