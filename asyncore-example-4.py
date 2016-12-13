import SimpleAsyncHTTP
import asyncore
class DummyConsumer:
    size = 0
    def http_header(self, request):
        # handle header
        if request.status is None:
            print "connection failed"
        else:
            print "status", "=>", request.status
            for key, value in request.header.items():
                print key, "=", value
    def feed(self, data):
        # handle incoming data
        self.size = self.size + len(data)
    def close(self):
        # end of data
        print self.size, "bytes in body"
class RedirectingConsumer:
    def __init__(self, consumer):
        self.consumer = consumer
    def http_header(self, request):
        # handle header
        if request.status is None or\
           request.status[1] not in ("301", "302"):
            try:
                http_header = self.consumer.http_header
            except AttributeError:
                pass
            else:
                return http_header(request)
        else:
            # redirect!
            uri = request.header["location"]
            print "redirecting to", uri, "..."
            request.close()
            SimpleAsyncHTTP.AsyncHTTP(uri, self)
    def feed(self, data):
        self.consumer.feed(data)
    def close(self):
        self.consumer.close()
#
# try it out
consumer = RedirectingConsumer(DummyConsumer())
request = SimpleAsyncHTTP.AsyncHTTP(
    "http://www.pythonware.com/library",
    consumer
    )
asyncore.loop()