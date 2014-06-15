import time
from RPi import GPIO
class eb21(object):
    board = {'p0':11, 'p1':12, 'p2':13, 'p3':15, 'p4':16, 'p5':18, 'p6':22, 'p7':7}
    bcm = {'p0':17, 'p1':18, 'p2':21, 'p3':22, 'p4':23, 'p5':24, 'p6':25, 'p7':4}
    m = ['LOW', 'HIGH']
    def setall(mode, s=0):
        for i in range(len(mode)):
            p = eb21.board['p'+str(s+i)]
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, mode[i])
    def status(mode = GPIO.IN):
        res = {}
        for name in eb21.board.keys():
            p = eb21.board[name]
            GPIO.setup(p, mode)
            res[name] = eb21.m[GPIO.input(p)]
        return res
    def set_pin(name, v):
        p = eb21.board[name]
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, v)
        return GPIO.input(eb21.board[name]) == v
    def get_pin(self, name):
        return eb21.m[GPIO.input(eb21.board[name])]
    def rev_pin(name):
        p = eb21.board[name]
        GPIO.setup(p, GPIO.OUT)
        tmpv = GPIO.input(p)
        GPIO.output(p, not GPIO.input(p))
        return GPIO.input(eb21.board[name]) != tmpv

if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    eb21.setall((0,0,0,0,0,0,0))
    print(eb21.status())
    name = 'p'+input('number of pin:')
    while(name in eb21.board.keys()):
        if(eb21.rev_pin(name)):
            print(eb21.m[GPIO.input(eb21.board[name])])
            print(eb21.status(GPIO.OUT))
            name = 'p' + input('number of pin:')
        else:
            print('error')
    print(eb21.status(GPIO.OUT))
    for name in eb21.board.keys():
        eb21.rev_pin(name)
    time.sleep(2)
    print(eb21.status())
    eb21.setall((0,0,0,0,0,0,0))
    GPIO.cleanup()
    print(eb21.status())
