#coding=UTF-8
import md5
import string, random
def getchallenge():
    # generate a 16-byte long random string.  (note that the built-
    # in pseudo-random generator uses a 24-bit seed, so this is not
    # as good as it may seem...)
# 生成一个 16 字节长的随机字符串. 注意内建的伪随机生成器
# 使用的是 24 位的种子(seed), 所以这里这样用并不好..
    challenge = map(lambda i: chr(random.randint(0, 255)), range(16))
    return string.join(challenge, "")

def getresponse(password, challenge):
# calculate combined digest for password and challenge # 计算密码和质询(challenge)的联合密文
    m = md5.new()
    m.update(password)
    m.update(challenge)
    return m.digest()
#
# server/client communication # 服务器/客户端通讯
# 1. client connects. server issues challenge. # 1. 客户端连接, 服务器发布质询(challenge)
print "client:", "connect"
challenge = getchallenge()
print "server:", repr(challenge)
# 2. client combines password and challenge, and calculates # the response.
# 2. 客户端计算密码和质询(challenge)的组合后的密文
client_response = getresponse("trustno1", challenge)
print "client:", repr(client_response)
# 3. server does the same, and compares the result with the # client response. the result is a safe login in which the # password is never sent across the communication channel. # 3. 服务器做同样的事, 然后比较结果与客户端的返回,
# 判断是否允许用户登陆. 这样做密码没有在通讯中明文传输.
server_response = getresponse("trustno1", challenge)
if server_response == client_response:
    print "server:", "login ok"