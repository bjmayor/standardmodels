import asyncore, asynchat
import os, socket, string, sys
import StringIO, mimetools

ROOT = "."
PORT = 8000

class HTTPChannel(asynchat.async_chat):
    def __init__(self, server, sock, addr):
        asynchat.async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\r\n\r\n')
        self.header = None
        self.data = ""
        self.shutdown = 0

    def collect_incoming_data(self, data):
        self.data = self.data + data
        if len(self.data) > 16384:
            self.shutdown = 1

    def found_terminator(self):
        if not self.header:
            fp = StringIO.StringIO(self.data)
            print self.data
            request = string.split(fp.readline(), None, 2)
            print request
            if len(request) !=3:
                self.shutdown = 1
            else:
                self.header = mimetools.Message(fp)
                self.set_terminator("\r\n")
                self.server.handle_request(self, request[0], request[1], self.header)
                self.close_when_done()
            self.data = ""
        else:
            pass

    def pushstatus(self, status, explanation="OK"):
        self.push("HTTP/1.0 %d %s\r\n" % (status, explanation))

class FileProducer:
    def __init__(self, file):
        self.file = file

    def more(self):
        if self.file:
            data = self.file.read(2048)
            if data:
                return data
            self.file = None
        return ""

class HTTPServer(asyncore.dispatcher):
    def __init__(self, port=None, request=None):
        if not port:
            port = 80
        self.port = port
        if request:
            self.handle_request = request
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(("", port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        HTTPChannel(self, conn, addr)

    def handle_request(self, channel, method, path, header):
        try:
            while path[:1] == "/":
                path = path[1:]
            filename = os.path.join(ROOT, path)
            print path, "=>", filename
            file = open(filename,"r")
        except IOError:
            channel.pushstatus(404, "Not found")
            channel.push("Content-type: text/html\r\n")
            channel.push("\r\n")
            channel.push("<html><body>File not found.</body></html>\r\n")
        else:
            channel.pushstatus(200,"OK")
            channel.push("Content-type: text/html\r\n")
            channel.push("\r\n")
            channel.push_with_producer(FileProducer(file))


s = HTTPServer(PORT)
print  "serving at port", PORT
asyncore.loop()
