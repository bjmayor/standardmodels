import cStringIO
MESSAGE = "That man is depriving a village somewhere of a computer scientist."
file = cStringIO.StringIO(MESSAGE)

print file.read()