import robotparser
r = robotparser.RobotFileParser()
r.set_url("http://www.python.org/robots.txt")
r.read()
if r.can_fetch("*", "/index.html"):
    print "may fetch the home page"
if r.can_fetch("*", "/tim_one/index.html"):
    print "may fetch the tim peters archive"