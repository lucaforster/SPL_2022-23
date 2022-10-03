import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
while True:
        print("Schreibe e um einzuschalten und a um auszaschalten")
        Eingabe = input()
        if Eingabe == "a":
                GPIO.output(3, False)
        elif Eingabe == "e":
                GPIO.output(3, True)
        else:
                print("Es wurde weder e noch a eingegeben")
