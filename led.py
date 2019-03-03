import RPi.GPIO as GPIO
import time
import sys
from GCStatic import eb21

def blink(i, mode='board'):
    if(mode == 'board'):
        GPIO.setmode(GPIO.BOARD)
        p = eb21.board['p'+str(i)]
    elif(mode == 'bcm'):
        GPIO.setmode(GPIO.BCM)
        p = eb21.bcm['p'+str(i)]
    print(i, p)
    GPIO.setup(p, GPIO.OUT)
#        GPIO.output(p, GPIO.HIGH) #or output(11, GPIO.True)
#        time.sleep(1)
#        GPIO.output(p, GPIO.LOW)
    for t in range(5):
        GPIO.output(p, not GPIO.input(p))
        time.sleep(0.5)
    GPIO.output(p, GPIO.LOW)

if __name__ == '__main__':
#    mod = 'board'
    mod = 'bcm'
    GPIO.cleanup()
    print(mod)
    if 1 == len(sys.argv):
        for i in range(8):
            blink(i, mod)
    else:
        while True:
            blink(int(sys.argv[1]), mod)
    GPIO.cleanup()
    print('end')
