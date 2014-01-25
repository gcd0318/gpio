from RPi import GPIO
from GCStatic import eb21
import time

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
ttl = eb21.board[5]
GPIO.setup(ttl, GPIO.IN)
while True:
    if(GPIO.input(ttl)):
        print('shaking')
#    else:
#        print('ok')
    time.sleep(0.1)
