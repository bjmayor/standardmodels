import rotor
SECRET_KEY = "spam"
MESSAGE = "the holy grail"
r = rotor.newrotor(SECRET_KEY)
encoded_message = r.encrypt(MESSAGE)
decoded_message = r.decrypt(encoded_message)

print "original:", repr(MESSAGE)
print "encoded message:", repr(encoded_message)
print "decoded message:", repr(decoded_message)