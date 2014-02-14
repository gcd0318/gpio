from RPi import GPIO
from GCStatic import eb21
import time
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
RED_PIN = eb21.board[0]
GREEN_PIN = eb21.board[1]
BLUE_PIN = eb21.board[2]

speed=0.02
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
RED_PWM = GPIO.PWM(RED_PIN,255)
GREEN_PWM =GPIO.PWM(GREEN_PIN,255)
BLUE_PWM =GPIO.PWM(BLUE_PIN,255)
RED_PWM.start(0)
GREEN_PWM.start(0)
BLUE_PWM.start(0)
r=0
g=0
b=0
for i in range(0, 100, 1):
        r1=random.randint(0, 255)
        g1=random.randint(0, 255)
        b1=random.randint(0, 255)
        dr=(r1-r)/100
        dg=(g1-g)/100
        db=(b1-b)/100
        for i in range(0, 99, 1):
                RED=100-r/2.55
                GREEN=100-g/2.55
                BLUE=100-b/2.55
                RED_PWM.ChangeDutyCycle(RED)
                GREEN_PWM.ChangeDutyCycle(GREEN)
                BLUE_PWM.ChangeDutyCycle(BLUE)
                r=r+dr
                g=g+dg
                b=b+db
                time.sleep(speed)
RED_PWM.stop()
GREEN_PWM.stop()
BLUE_PWM.stop()
GPIO.output(RED_PIN,1)
GPIO.output(GREEN_PIN,1)
GPIO.output(BLUE_PIN,1)
GPIO.cleanup()
