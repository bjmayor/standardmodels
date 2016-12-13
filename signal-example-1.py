import signal
import time
def handler(signo, frame):
    print "got signal", signo
signal.signal(signal.SIGALRM, handler)
# wake me up in two seconds
signal.alarm(2)

now = time.time()
time.sleep(200)
print "slept for", time.time() - now, "seconds"