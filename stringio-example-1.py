import StringIO
MESSAGE = "That man is depriving a village somewhere of a computer scientist."
file = StringIO.StringIO(MESSAGE)
print file.read()