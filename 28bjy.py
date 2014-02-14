from RPi import GPIO
import time
from GCStatic import eb21

def run(mode):
    if(mode == 'board'):
        GPIO.setmode(GPIO.BOARD)
    elif(mode == 'bcm'):
        GPIO.setmode(GPIO.BCM)
    while(True):
        eb21.setall((1,0,0,0))
        eb21.setall((0,0,1,0))
        eb21.setall((0,1,0,0))
        eb21.setall((0,0,0,1))

if __name__ == '__main__':
    GPIO.cleanup()
    run('board')

