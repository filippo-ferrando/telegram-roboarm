import RPi.GPIO as GPIO
import time

servoPin = x #sostituisci con il pin del servo

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)
p.start(2.5)

try:
    while True:
        p.ChangeDutyCicle(5)
        time.sleep(0.5)
        p.ChangeDutyCicle(10)
        time.sleep(0.5)
        p.ChangeDutyCicle(15)
        time.sleep(0.5)
        p.ChangeDutyCicle(20)
        time.sleep(0.5)
        p.ChangeDutyCicle(25)
        time.sleep(0.5)
        p.ChangeDutyCicle(30)
        time.sleep(0.5)
        p.ChangeDutyCicle(35)
        time.sleep(0.5)
        p.ChangeDutyCicle(40)
        time.sleep(0.5)
        p.ChangeDutyCicle(45)
        time.sleep(0.5)
        p.ChangeDutyCicle(50)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
        