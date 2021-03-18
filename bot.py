import sys
import time
import random
import datetime
import telepot
from gpiozero import Servo


#servo1Pin = Servo(17) #sostituisci con il pin del servo
#servo2Pin = Servo(18)
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

DEFAULT = 0

global servo1val, servo2val, servo3val

def gira(pin, dutyCicle):
    global servo1val, servo2val, servo3val
    if pin == "1":
        #servo1Pin.value(dutyCicle)
        print(f"Muovo 1 servo di {dutyCicle}")
        servo1val = dutyCicle
    elif pin == "2":
        #servo2Pin.value(dutyCicle)
        print(f"Muovo 2 servo di {dutyCicle}")
        servo2val = dutyCicle
    elif pin == "3":
        #p3.ChangeDutyCicle(dutyCicle)
        print(f"Muovo 3 servo di {dutyCicle}")
        servo3val = dutyCicle

def handle(msg):
    global servo1val, servo2val, servo3val

    chat_id = msg['chat']['id']
    command = msg['text']

    comandoCompleto = command.split(',')

    if comandoCompleto[-1] == 'info':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 1 --> " + str(servo1val))
        bot.sendMessage(chat_id, "Servo 2 --> " + str(servo2val))
        bot.sendMessage(chat_id, "Servo 3 --> " + str(servo3val))

    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'primo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 1 --> " + str(servo1val))
    
    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'secondo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 2 --> " + str(servo2val))

    if comandoCompleto[0] == 'info' and comandoCompleto[-1] == 'terzo':
        bot.sendMessage(chat_id, "Sending info: ")
        bot.sendMessage(chat_id, "Servo 3 --> " + str(servo3val))


    if comandoCompleto[0] == 'reset':
        bot.sendMessage(chat_id, "Azzero i servo")
        gira("1", DEFAULT)
        gira("2", DEFAULT)
        gira("3", DEFAULT)
        servo1val = DEFAULT
        servo2val = DEFAULT
        servo3val = DEFAULT

    if comandoCompleto[0] == 'primo':
        bot.sendMessage(chat_id, "Muovo primo servo di " + str(comandoCompleto[-1]))
        gira("1", comandoCompleto[-1])

    if comandoCompleto[0] == 'secondo':
        bot.sendMessage(chat_id, "Muovo secondo servo di " + str(comandoCompleto[-1]))
        gira("2", comandoCompleto[-1])

    if comandoCompleto[0] == 'terzo':
        bot.sendMessage(chat_id, "Muovo terzo servo di " + str(comandoCompleto[-1]))
        gira("3", comandoCompleto[-1])


bot = telepot.Bot('1608661768:AAGFN2sY7j61NbkXKVVAqhMaNSMQyU6f7fA')
bot.message_loop(handle)

print("Listening...")

while 1:
    time.sleep(1)
