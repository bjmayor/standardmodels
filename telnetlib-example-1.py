import telnetlib
import sys
HOST = "123.56.99.154"
USER = "study"
PASSWORD = "study"
telnet = telnetlib.Telnet(HOST)
telnet.read_until("login: ")
telnet.write(USER + "\n")
telnet.read_until("Password: ")
telnet.write(PASSWORD + "\n")
telnet.write("ls \n")
telnet.write("exit\n")
print telnet.read_all()