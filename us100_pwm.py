from RPi import GPIO
import time, datetime
from GCStatic import eb21

def meters(tx, rx):
    while(not GPIO.input(rx)):
        t1 = datetime.datetime.now()
    while(GPIO.input(rx)):
        t2 = datetime.datetime.now()
#    if(t1 and t2)and(t1 < t2):
    if(t1 < t2):
        res = (t2-t1).microseconds
    else:
        res = 0
    return res/1000000*340/2

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
close = eb21.board['p0']
cn = 0.1
near = eb21.board['p1']
nm = 0.2
middle = eb21.board['p2']
mf = 0.3
far = eb21.board['p3']
fa = 0.4
away = eb21.board['p4']
error = eb21.board['p5']
for i in range(5+1):
    GPIO.setup(eb21.board['p'+str(i)], GPIO.OUT)
    GPIO.output(eb21.board['p'+str(i)], GPIO.LOW)

for i in range(2):
    eb21.setall((1,0,1,0,1,0))
    time.sleep(1)    
    eb21.setall((0,1,0,1,0,1))
    time.sleep(1)
eb21.setall((0,0,0,0,0,0))

tx = eb21.board['p6']
rx = eb21.board['p7']
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
    d = ((t2-t1).microseconds)/1000000*340/2
    if(0 < d):
        print(d)
        if((0 < d)and(d < cn)):
            eb21.setall((1,0,0,0,0,0))
        elif((cn <= d)and(d < nm)):
            eb21.setall((0,1,0,0,0,0))
        elif((nm <= d)and(d < mf)):
            eb21.setall((0,0,1,0,0,0))
        elif((mf <= d)and(d < fa)):
            eb21.setall((0,0,0,1,0,0))
        elif(fa <= d):
            eb21.setall((0,0,0,0,1,0))
        else:
            eb21.setall((1,0,0,0,0,1))
    else:
        print('finding')
