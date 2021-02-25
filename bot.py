import sys
import time
import random
import datetime
import telepot
#import Rpi.GPIO as GPIO


#servo1Pin = x #sostituisci con il pin del servo
#servo2Pin = x2
#servo3Pin = x2

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(servo1PIN, GPIO.OUT)
#GPIO.setup(servo2PIN, GPIO.OUT)
#GPIO.setup(servo3PIN, GPIO.OUT)

#p1 = GPIO.PWM(servo1Pin, 50)
#p1.start(2.5)

#p2 = GPIO.PWM(servo2Pin, 50)
#p2.start(2.5)

#p3 = GPIO.PWM(servo3Pin, 50)
#p3.start(2.5)

def gira(pin, dutyCicle):
    if pin == "1":
        #p1.ChangeDutyCicle(dutyCicle)
        print(f"moving 1 servo di {dutyCicle}")
    elif pin == "2":
        #p2.ChangeDutyCicle(dutyCicle)
        print(f"moving 2 servo di {dutyCicle}")
    elif pin == "3":
        #p3.ChangeDutyCicle(dutyCicle)
        print(f"moving 3 servo di {dutyCicle}")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    comandoCompleto = command.split(',')

    if comandoCompleto[0] == 'primo':
        bot.sendMessage(chat_id, "Muovo primo servo")
        gira("1", comandoCompleto[-1])

    if comandoCompleto[0] == 'secondo':
        bot.sendMessage(chat_id, "Muovo secondo servo")
        gira("2", comandoCompleto[-1])

    if comandoCompleto[0] == 'terzo':
        bot.sendMessage(chat_id, "Muovo terzo servo")
        gira("3", comandoCompleto[-1])


bot = telepot.Bot('1608661768:AAGFN2sY7j61NbkXKVVAqhMaNSMQyU6f7fA')
bot.message_loop(handle)

print("Listening...")

while 1:
    time.sleep(1)
