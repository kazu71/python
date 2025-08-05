import RPi.GPIO as GPIO
from time import sleep

print("system ok")




GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    #LED0.5秒間隔で点灯・消灯
    while True:
        GPIO.output(17, GPIO.HIGH)
        print("LED on")
        sleep(0.5)
        GPIO.output(17, GPIO.LOW)
        print("LED OFF")
        sleep(0.5)
        GPIO.output(17, GPIO.HIGH)
        print("LED on")
        sleep(0.1)
        GPIO.output(17, GPIO.LOW)
        print("LED OFF")
        sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
