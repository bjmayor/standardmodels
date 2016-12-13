import httplib
USER_AGENT = "httplib-example-1.py"
class Error:
    # indicates an HTTP error
    def __init__(self, url, errcode, errmsg, headers):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg
        self.headers = headers
    def __repr__(self):
        return (
            "<Error for %s: %s %s>" %
            (self.url, self.errcode, self.errmsg)
            )
class Server:
    def __init__(self, host):
        self.host = host
    def fetch(self, path):
        http = httplib.HTTP(self.host)
        # write header
        http.putrequest("GET", path)
        http.putheader("User-Agent", USER_AGENT)
        http.putheader("Host", self.host)
        http.putheader("Accept", "*/*")
        http.endheaders()
        # get response
        errcode, errmsg, headers = http.getreply()
        if errcode != 200:
            raise Error(path,errcode, errmsg, headers)
        file = http.getfile()
        return file.read()
if __name__ == "__main__":
    server = Server("go2live.cn")
    print server.fetch("/archives/150924.html")