import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

GPIO.output(7, True)
GPIO.output(3, False)

Status = True
while True:
        Eingabe = int(input())
        if Eingabe == 1 and Status == True:
                GPIO.output(5, True)
                GPIO.output(7, True)
                time.sleep(3.5)
                GPIO.output(5, False)
                GPIO.output(7, False)
                GPIO.output(3, True)
                Status = False
        elif Eingabe == 1 and Status == False:
                i = 0
                while i < 4:
                        GPIO.output(3, True)
                        time.sleep(0.5)
                        GPIO.output(3, False)
                        time.sleep(0.5)
                        i = i +1
                GPIO.output(5, True)
                time.sleep(3.5)
                GPIO.output(5, False)
                GPIO.output(7, True)
                Status = True
        else:
                print("Unbekannte Eingabe")

