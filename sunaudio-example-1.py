import sunaudio
file = "samples/sample.au"
print sunaudio.gethdr(open(file, "rb"))