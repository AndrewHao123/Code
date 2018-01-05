import RPi.GPIO as GPIO
import time, datetime

GPIO_PIN = 17
count = 0


GPIO.setmode(GPIO.BCM)
##GPIO.setup(GPIO_PIN, GPIO.IN)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

##print("waiting 5 times...")

while True:
    if(GPIO.input(GPIO_PIN) == 0):
        #start = time.time.clock()
        count = count + 1
        #end = time.time.clock()
##        print("input high")
##    else:
        print("Counter is " , count)
        ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S,%f'
        now = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        #now = time.shrftime("%Y-%m-%d %H:%M:%S:%MS")

        print(" It's " , now)
        time.sleep(1)
##    time.sleep(0.1)

print("exit...")
GPIO.cleanup()

