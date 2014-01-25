import time
from RPi import GPIO
class eb21(object):
    board = {0:11, 1:12, 2:13, 3:15, 4:16, 5:18, 6:22, 7:7}
    bcm = {0:17, 1:18, 2:21, 3:22, 4:23, 5:24, 6:25, 7:4}
    m = ['LOW', 'HIGH']
    def setall(mod, s=0):
        for i in range(len(mod)):
            p = eb21.board[s+i]
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, mod[i])
    def status(mode = GPIO.IN):
        res = {}
        for i in eb21.board.keys():
            p = eb21.board[i]
            GPIO.setup(p, mode)
            res[i] = eb21.m[GPIO.input(p)]
        return res
    def set_pin(i, v):
        p = eb21.board[i]
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, v)
        return GPIO.input(eb21.board[i]) == v
    def get_pin(self, i):
        return eb21.m[GPIO.input(p)]
    def rev_pin(i):
        p = eb21.board[i]
        GPIO.setup(p, GPIO.OUT)
        tmpv = GPIO.input(p)
        GPIO.output(p, not GPIO.input(p))
        return GPIO.input(eb21.board[i]) != tmpv

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    eb21.setall((0,0,0,0,0,0,0))
    print(eb21.status())
    i = int(input('number of pin:'))
    while(i in eb21.board.keys()):
        if(eb21.rev_pin(i)):
            print(eb21.m[GPIO.input(eb21.board[i])])
            print(eb21.status(GPIO.OUT))
            i = int(input('number of pin:'))
        else:
            print('error')
    print(eb21.status(GPIO.OUT))
    for i in eb21.board.keys():
        eb21.rev_pin(i)
    time.sleep(2)
    print(eb21.status())
    eb21.setall((0,0,0,0,0,0,0))
    GPIO.cleanup()
    print(eb21.status())
