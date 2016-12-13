import socket
import struct, time
# user-accessible port
PORT = 8037
# reference time
TIME1970 = 2208988800L
# establish server
service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
service.bind(("", PORT))
print "listening on port", PORT
while 1:
    # serve forever
    data, client = service.recvfrom(0)
    print "connection from", client
    t = int(time.time()) + TIME1970
    t = struct.pack("!I", t)
    service.sendto(t, client) # send timestamp