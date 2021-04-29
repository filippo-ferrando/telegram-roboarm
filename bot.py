import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO


servo1PIN = 17 #sostituisci con il pin del servo
servo2PIN = 18
servo3PIN = 27
servo4PIN = 22
servo5PIN = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo1PIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)
GPIO.setup(servo3PIN, GPIO.OUT)
GPIO.setup(servo4PIN, GPIO.OUT)
GPIO.setup(servo5PIN, GPIO.OUT)

p1 = GPIO.PWM(servo1PIN, 50)
p1.start(2.5)

p2 = GPIO.PWM(servo2PIN, 50)
p2.start(2.5)

p3 = GPIO.PWM(servo3PIN, 50)
p3.start(2.5)

p4 = GPIO.PWM(servo4PIN, 50)
p4.start(2.5)

p5 = GPIO.PWM(servo5PIN, 50)
p5.start(2.5)

DEFAULT = 2.5

global servo1val, servo2val, servo3val, servo4val, servo5val

servo1val = DEFAULT
p1.ChangeDutyCycle(2.5)

servo2val = DEFAULT
p2.ChangeDutyCycle(2.5)

servo3val = DEFAULT
p3.ChangeDutyCycle(2.5)

servo4val = DEFAULT
p4.ChangeDutyCycle(2.5)

servo5val = DEFAULT
p5.ChangeDutyCycle(2.5)

def gira(pin, dutyCicle):
    global servo1val, servo2val, servo3val, servo4val, servo5val
    if pin == "1":
        p1.ChangeDutyCycle(dutyCicle)
        print(f"Muovo 1 servo di {dutyCicle}")
        servo1val = dutyCicle
    elif pin == "2":
        p2.ChangeDutyCycle(dutyCicle)
        print(f"Muovo 2 servo di {dutyCicle}")
        servo2val = dutyCicle
    elif pin == "3":
        p3.ChangeDutyCycle(dutyCicle)
        print(f"Muovo 3 servo di {dutyCicle}")
        servo3val = dutyCicle
    elif pin == "4":
        p4.ChangeDutyCycle(dutyCicle)
        print(f"Muovo 4 servo di {dutyCicle}")
    elif pin == "5":
        p5.ChangeDutyCycle(dutyCicle)
        print(f"Muovo 5 servo di {dutyCicle}")

def reset():
    global servo1val, servo2val, servo3val, servo4val, servo5val
    gira("1", DEFAULT)
    gira("2", DEFAULT)
    gira("3", DEFAULT)
    gira("4", DEFAULT)
    gira("5", DEFAULT)
    servo1val = DEFAULT
    servo2val = DEFAULT
    servo3val = DEFAULT
    servo4val = DEFAULT
    servo5val = DEFAULT
    print("resettato")


def handle(msg):
    global servo1val, servo2val, servo3val, servo4val, servo5val

    servo5val=DEFAULT
    servo4val=DEFAULT
    servo2val=DEFAULT
    servo3val=DEFAULT
    servo1val=DEFAULT

    chat_id = msg['chat']['id']
    command = msg['text']

    comandoCompleto = command.split(',')

    # -- INFO FOR ALL SERVO --
    if comandoCompleto[-1] == 'info':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 1 --> " + str(servo1val))
        bot.sendMessage(chat_id, "Servo 2 --> " + str(servo2val))
        bot.sendMessage(chat_id, "Servo 3 --> " + str(servo3val))
        bot.sendMessage(chat_id, "Servo 4 --> " + str(servo4val))
        bot.sendMessage(chat_id, "Servo 5 --> " + str(servo5val))
    # -- FINISH BLOCK --

    # -- INFO FOR SINGLE SERVO --
    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'primo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 1 --> " + str(servo1val))
    
    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'secondo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 2 --> " + str(servo2val))

    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'terzo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 3 --> " + str(servo3val))

    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'quarto':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 4 --> " + str(servo4val))

    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'quinto':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 5 --> " + str(servo5val))
    # -- FINISH BLOCK --

    # -- RESET ALL SERVO --
    if comandoCompleto[0] == 'reset':
        bot.sendMessage(chat_id, "Azzero i servo")
        reset()
    # -- FINISH BLOCK --
        
    # -- MOVE SERVO --
    if comandoCompleto[0] == 'primo':
        bot.sendMessage(chat_id, "Muovo primo servo di " + str(comandoCompleto[-1]))
        gira("1", (float(comandoCompleto[-1])/18)+2)

    if comandoCompleto[0] == 'secondo':
        bot.sendMessage(chat_id, "Muovo secondo servo di " + str(comandoCompleto[-1]))
        gira("2", (float(comandoCompleto[-1])/18)+2)

    if comandoCompleto[0] == 'terzo':
        bot.sendMessage(chat_id, "Muovo terzo servo di " + str(comandoCompleto[-1]))
        gira("3", (float(comandoCompleto[-1])/18)+2)

    if comandoCompleto[0] == 'quarto':
        bot.sendMessage(chat_id, "Muovo quarto servo di " + str(comandoCompleto[-1]))
        gira("4", (float(comandoCompleto[-1])/18)+2)

    if comandoCompleto[0] == 'quinto':
        bot.sendMessage(chat_id, "Muovo quinto servo di " + str(comandoCompleto[-1]))
        gira("5", (float(comandoCompleto[-1])/18)+2)
    # -- FINISH BLOCK --


    # -- FUNCTION SECTION --

    # -- FINISH BLOCK --



bot = telepot.Bot('1617506018:AAGUkkTv9ScB9eN8uNp6xiM0g9F9vWJguHo')
bot.message_loop(handle)

print("Listening...")

while 1:
    time.sleep(1)
