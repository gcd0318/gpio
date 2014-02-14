from RPi import GPIO
from GCStatic import eb21
import time

GPIO.setmode(GPIO.BOARD)
for i in range(8):
    GPIO.setup(eb21.board[i], GPIO.OUT)
    p = GPIO.PWM(eb21.board[i], 0.50)
    p.start(1)
    input('enter for change mode')
    p.stop()
    try:
        p = GPIO.PWM(eb21.board[i], 50)
        p.start(0)
        while True:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        p.stop()
GPIO.cleanup()
