import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
while True:
        GPIO.output(3,True)
        time.sleep(4)
        GPIO.output(3,False)
        time.sleep(2)
        GPIO.output(3, True)
        time.sleep(1)
        GPIO.output(3, False)
        time.sleep(2)
        GPIO.output(3, True)
        time.sleep(1)
        GPIO.output(3, False)
        time.sleep(2)