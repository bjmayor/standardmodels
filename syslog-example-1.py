import syslog
import sys
syslog.openlog(sys.argv[0])
syslog.syslog(syslog.LOG_NOTICE, "a log notice")
syslog.syslog(syslog.LOG_NOTICE, "another log notice: %s" % "watch out!")

syslog.closelog()