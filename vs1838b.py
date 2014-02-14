import RPi.GPIO as GPIO
import time
from GCStatic import eb21

def get_signal(mode, i):
    res = ''
    if(mode == 'board'):
        GPIO.setmode(GPIO.BOARD)
        p = eb21.board[i]
    elif(mode == 'bcm'):
        GPIO.setmode(GPIO.BCM)
        p = eb21.bcm[i]
    print(i, p)
    GPIO.setup(p, GPIO.IN)
    res = GPIO.input(p)
    while(res == GPIO.input(p)):
        time.sleep(0.1)
    res = GPIO.input(p)
    return res

if __name__ == '__main__':
    GPIO.cleanup()
    i = 7
    GPIO.setmode(GPIO.BOARD)
    print('board', i)
    while True:
        print(get_signal('board', i))
#    print('bcm')
#    blink('bcm')
    GPIO.cleanup()
    print('end')
