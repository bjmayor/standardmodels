import netrc
# default is $HOME/.netrc
info = netrc.netrc("samples/sample.netrc")
login, account, password = info.authenticators("secret.fbi")
print "login", "=>", repr(login)
print "account", "=>", repr(account)
print "password", "=>", repr(password)
