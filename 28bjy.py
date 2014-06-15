from RPi import GPIO
import time
from GCStatic import eb21

def run(mode='board', step=4, idle=0):
    if(mode == 'board'):
        GPIO.setmode(GPIO.BOARD)
    elif(mode == 'bcm'):
        GPIO.setmode(GPIO.BCM)
    while(True):
        if(4 == step):
            eb21.setall((1,0,0,0))
            time.sleep(idle)
            eb21.setall((0,1,0,0))
            time.sleep(idle)
            eb21.setall((0,0,1,0))
            time.sleep(idle)
            eb21.setall((0,0,0,1))
            time.sleep(idle)
        elif(8==step):
            eb21.setall((1,0,0,0))
            time.sleep(idle)
            eb21.setall((1,1,0,0))
            time.sleep(idle)
            eb21.setall((0,1,0,0))
            time.sleep(idle)
            eb21.setall((0,1,1,0))
            time.sleep(idle)
            eb21.setall((0,0,1,0))
            time.sleep(idle)
            eb21.setall((0,0,1,1))
            time.sleep(idle)
            eb21.setall((0,0,0,1))
            time.sleep(idle)
            eb21.setall((1,0,0,1))
            time.sleep(idle)

if __name__ == '__main__':
    GPIO.cleanup()
    run('board', 8, 0.01)
