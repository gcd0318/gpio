import RPi.GPIO as GPIO
import time, datetime
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
#    txpwm =  GPIO.PWM(p,10) 
#    txpwm.start(0.1)
    tx = eb21.board[6]
    rx = eb21.board[7]
    GPIO.setup(rx, GPIO.IN)
    GPIO.setup(tx, GPIO.OUT)
    GPIO.output(tx, GPIO.LOW)
    txpwm =  GPIO.PWM(tx,10)
    txpwm.start(0.1)
    while(True):
        while(not GPIO.input(rx)):
            pass
        t1 = datetime.datetime.now()
        while(GPIO.input(rx)):
            pass
        t2 = datetime.datetime.now()
        print(t2-t1)
                                
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
