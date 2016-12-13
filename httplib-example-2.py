import httplib
USER_AGENT = "httplib-example-2.py"
def post(host, path, data, type=None):
    http = httplib.HTTP(host)
    # write header
    http.putrequest("PUT", path)
    http.putheader("User-Agent", USER_AGENT)
    http.putheader("Host", host)
    if type:
        http.putheader("Content-Type", type)
    http.putheader("Content-Length", str(len(data)))
    http.endheaders()
    # write body
    http.send(data)
    # get response
    errcode, errmsg, headers = http.getreply()
    if errcode != 200:
        raise Exception(errcode, errmsg, headers)
    file = http.getfile()
    return file.read()
if __name__ == "__main__":
    post("www.spam.egg", "/bacon.htm", "a piece of data", "text/plain")