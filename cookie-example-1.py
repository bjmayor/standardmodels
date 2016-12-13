import Cookie
import os, time
cookie = Cookie.SimpleCookie()
cookie["user"] = "Mimi"
cookie["timestamp"] = time.time()
print cookie
# simulate CGI roundtrip
os.environ["HTTP_COOKIE"] = str(cookie)
print
cookie = Cookie.SmartCookie()
cookie.load(os.environ["HTTP_COOKIE"])
for key, item in cookie.items():
    # dictionary items are "Morsel" instances
    # use value attribute to get actual value
    print key, repr(item.value)