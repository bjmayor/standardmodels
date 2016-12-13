import socket
import struct, time
# user-accessible port
PORT = 8037
# reference time
TIME1970 = 2208988800L
# establish server
service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", PORT))
service.listen(1)
print "listening on port", PORT
while 1:
# serve forever
    channel, info = service.accept()
    print "connection from", info
    t = int(time.time()) + TIME1970
    t = struct.pack("!I", t)
    channel.send(t) # send timestamp
    channel.close() # disconnect