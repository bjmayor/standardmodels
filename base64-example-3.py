import base64
def getbasic(user, password):
    # basic authentication (according to HTTP)
    return base64.encodestring(user + ":" + password)
print getbasic("Aladdin", "open sesame")