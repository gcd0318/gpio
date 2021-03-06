from RPi import GPIO
import time, datetime
from GCStatic import eb21

def meters(tx, rx):
    t2 = datetime.datetime.now()
    GPIO.output(tx, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(tx, GPIO.LOW)
    t1 = datetime.datetime.now()
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
close = eb21.board[0]
cn = 0.1
near = eb21.board[1]
nm = 0.2
middle = eb21.board[2]
mf = 0.3
far = eb21.board[3]
fa = 0.4
away = eb21.board[4]
error = eb21.board[5]
for i in range(5+1):
    GPIO.setup(eb21.board[i], GPIO.OUT)
    GPIO.output(eb21.board[i], GPIO.LOW)

for i in range(2):
    eb21.setall((1,0,1,0,1,0))
    time.sleep(1)    
    eb21.setall((0,1,0,1,0,1))
    time.sleep(1)
eb21.setall((0,0,0,0,0,0))

tx = eb21.board[6]
rx = eb21.board[7]
GPIO.setup(rx, GPIO.IN)
GPIO.setup(tx, GPIO.OUT)
while(True):
    d = meters(tx, rx)
    if(0 < d):
        print(d)
    else:
        print('finding')
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
