from RPi import GPIO
from GCStatic import eb21
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(eb21.board[4], GPIO.OUT)

p = GPIO.PWM(eb21.board[4], 50)
p.start(0)
while True:
    for dc in range(0, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
p.stop()
GPIO.cleanup()
