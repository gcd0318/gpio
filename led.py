import RPi.GPIO as GPIO
import time
from GCStatic import eb21

def blink(mode='board'):
    for i in range(8):
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
    blink(mod)
#    print('bcm')
#    blink('bcm')
    GPIO.cleanup()
    print('end')
