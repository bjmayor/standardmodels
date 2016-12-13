import pwd, crypt
def login(user, password):
    "Check if user would be able to log in using password"
    try:
        pw1 = pwd.getpwnam(user)[1]
        pw2 = crypt.crypt(password, pw1[:2])
        return pw1 == pw2
    except KeyError:
        return 0 # no such user
user = raw_input("username:")
password = raw_input("password:")
if login(user, password):
    print "welcome", user
else:
    print "login failed"