class GPIO():
    pins = [0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0,\
            0, 0]
    inpins = []
    outpins = []
    m = ['LOW', 'HIGH']
    def cleanup():
        for i in range(len(GPIO.pins)):
            GPIO.pins[i] = 0
        GPIO.show()
        return 0

    def show():
        for i in range(len(GPIO.pins)//2):
            print(GPIO.pins[2*i], GPIO.pins[2*i+1])
        return 0

    def setup():

    def setmode():

    def 
