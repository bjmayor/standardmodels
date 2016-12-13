import audiodev
import aifc
sound = aifc.open("samples/sample.aiff", "r")
player = audiodev.AudioDev()
player.setoutrate(sound.getframerate())

player.setsampwidth(sound.getsampwidth())
player.setnchannels(sound.getnchannels())
bytes_per_frame = sound.getsampwidth() * sound.getnchannels()
bytes_per_second = sound.getframerate() * bytes_per_frame
while 1:
    data = sound.readframes(bytes_per_second)
    if not data:
        break
    player.writeframes(data)
player.wait()