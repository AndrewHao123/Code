# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
import RPi.GPIO as GPIO
import time

pin = 7                         ## 使用7号引脚
GPIO.setmode(GPIO.BOARD)        ## 使用BOARD引脚编号，此外还有 GPIO.BCM
GPIO.setup(pin, GPIO.OUT)       ## 设置7号引脚输出

while True:                          ## 重复
    GPIO.output(pin, GPIO.HIGH) ## 打开 GPIO 引脚（HIGH）
    time.sleep(1)               ## 等1秒
    GPIO.output(pin, GPIO.LOW)  ## 关闭 GPIO 引脚（LOW）
    time.sleep(1)               ## 等1秒

GPIO.cleanup()                   ## 清除
