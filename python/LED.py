import RPi.GPIO as GPIO
from time import sleep

print("system ok")



# GPIOの初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    #LEDを0.5秒おきに点灯・消灯
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
