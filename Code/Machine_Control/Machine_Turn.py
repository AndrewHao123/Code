#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO
import time
import atexit  
  
atexit.register(RPi.GPIO.cleanup) 

SG90_PIN = 18
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(SG90_PIN, RPi.GPIO.OUT)
SG90_PWM = RPi.GPIO.PWM(SG90_PIN, 50)#频率设为50HZ，一个比较舒服的频率
SG90_PWM.start(0)
try:
    while True:
        command = input("Please input 0 or 1:\n")
        if str(command) == "1":
            SG90_PWM.ChangeDutyCycle(2.5)
            time.sleep(0.02) 
            SG90_PWM.ChangeDutyCycle(0)
            time.sleep(0.02)
        elif str(command) == "0":
            SG90_PWM.ChangeDutyCycle(12.5)
            time.sleep(0.02)
            SG90_PWM.ChangeDutyCycle(0)
            time.sleep(0.02)
except KeyboardInterrupt:
    SG90_PWM.stop()
    RPi.GPIO.cleanup()
