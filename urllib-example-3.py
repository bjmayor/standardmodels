import urllib
class myURLOpener(urllib.FancyURLopener):
    # read an URL, with automatic HTTP authentication
    def setpasswd(self, user, passwd):
        self.__user = user
        self.__passwd = passwd
    def prompt_user_passwd(self, host, realm):
        return self.__user, self.__passwd
urlopener = myURLOpener()
urlopener.setpasswd("test", "test123")
#因为ua限制,都是403
fp = urlopener.open("http://go2live.cn")
print fp.read()