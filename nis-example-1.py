import nis
import string
print nis.cat("ypservers")
print string.split(nis.match("bacon", "hosts.byname"))