import RPi.GPIO as GPIO
import time

GPIO_PIN = 24
count = 500

GPIO.setmode(GPIO.BCM)
##GPIO.setup(GPIO_PIN, GPIO.IN)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("waiting 5 times...")

while count > 0:
    if(GPIO.input(GPIO_PIN) == 1):
        count = count - 1
        print("input high")
    else:
        print("input low")
    time.sleep(0.1)

print("exit...")
GPIO.cleanup()
