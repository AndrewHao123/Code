# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
import time
import RPi.GPIO as GPIO   #引入库
GPIO.setmode(GPIO.BOARD)  #设置编号方式
GPIO.setup(12, GPIO.OUT)  #设置12号引脚为输出模式

p = GPIO.PWM(12, 50)  #将12号引脚初始化为PWM实例 ，频率为50Hz
p.start(0)    #开始脉宽调制，参数范围为： (0.0 <= dc <= 100.0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)   #修改占空比 参数范围为： (0.0 <= dc <= 100.0)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()    #停止输出PWM波
GPIO.cleanup()    #清除





