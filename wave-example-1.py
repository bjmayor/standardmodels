import wave
w = wave.open("samples/sample.wav", "r")
if w.getnchannels() == 1:
    print "mono,",
else:
    print "stereo,",
print w.getsampwidth()*8, "bits,",
print w.getframerate(), "Hz sampling rate"