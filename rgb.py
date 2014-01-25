from RPi import GPIO
from GCStatic import eb21
import time



GPIO.setmode(GPIO.BOARD)
GPIO.setup(eb21.board[4], GPIO.OUT)

p = GPIO.PWM(eb21.board[4], 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()


"""
r = eb21.board[3]
g = eb21.board[2]
b = eb21.board[4]

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.output(r, GPIO.LOW)
GPIO.output(g, GPIO.LOW)
GPIO.output(b, GPIO.LOW)
rpwm = GPIO.PWM(r,1)
gpwm =GPIO.PWM(g,1)
bpwm =GPIO.PWM(b,1)
#rpwm.start(0)
#gpwm.start(0)
#bpwm.start(0)
dr = 0
dg = 0
db = 0

rpwm.start(1)
gpwm.start(1)
bpwm.start(1)

input('Press return to stop:')
rpwm.stop()
GPIO.cleanup()
"""
