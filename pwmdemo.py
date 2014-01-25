from RPi import GPIO
from GCStatic import eb21
import time
import random
GPIO.setwarnings(False)#禁止占用提示
GPIO.setmode(GPIO.BOARD)#设置GPIO针脚编号模式为板载编号
#——————可修改部分————
#设置红绿蓝针脚
RED_PIN = eb21.board[3]
GREEN_PIN = eb21.board[2]
BLUE_PIN = eb21.board[4]

#设置切换速度
speed=0.02
#————以下请勿修改，除非你知道各参数的意义————
GPIO.setup(RED_PIN, GPIO.OUT)#GPIO模式设置
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
RED_PWM = GPIO.PWM(RED_PIN,255)#启用PWM调制颜色
GREEN_PWM =GPIO.PWM(GREEN_PIN,255)
BLUE_PWM =GPIO.PWM(BLUE_PIN,255)
RED_PWM.start(0)
GREEN_PWM.start(0)
BLUE_PWM.start(0)
r=0#初始化RGB分量
g=0
b=0
for i in range(0, 100, 1):
        r1=random.randint(0, 255)#生成下一个随机颜色
        g1=random.randint(0, 255)
        b1=random.randint(0, 255)
        dr=(r1-r)/100#计算RGB各分量的增量，100为变化幅度
        dg=(g1-g)/100
        db=(b1-b)/100
        for i in range(0, 99, 1):#输出渐变颜色
                RED=100-r/2.55 #RGB颜色换算成占空比
                GREEN=100-g/2.55
                BLUE=100-b/2.55
                RED_PWM.ChangeDutyCycle(RED)#更改占空比
                GREEN_PWM.ChangeDutyCycle(GREEN)
                BLUE_PWM.ChangeDutyCycle(BLUE)
                r=r+dr#RGB分量各分量+增量
                g=g+dg
                b=b+db
                time.sleep(speed)#每种渐变颜色停留时间
RED_PWM.stop()#停止PWM调制
GREEN_PWM.stop()
BLUE_PWM.stop()
GPIO.output(RED_PIN,1)#关闭RGB_LED
GPIO.output(GREEN_PIN,1)
GPIO.output(BLUE_PIN,1)
GPIO.cleanup()#清除GPIO通道
