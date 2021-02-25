import requests
import datetime
#import Rpi.GPIO as GPIO
import time

#servoPin = x #sostituisci con il pin del servo

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)

#p = GPIO.PWM(servoPin, 50)
#p.start(2.5)

class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1608661768:AAGFN2sY7j61NbkXKVVAqhMaNSMQyU6f7fA' #Token of your bot
chatbot_bot = BotHandler(token) #Your bot's name

def main():
    new_offset = 0
    servoChoices = -1 # 1 -> primo servo, 2-> secondo servo, 3 -> terzo servo
    print('hi, now launching...')

    while True:
        all_updates=chatbot_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == '1':
                    chatbot_bot.send_message(first_chat_id, 'servo 1 selezionato' + first_chat_name)
                    servoChoices = 1
                    new_offset = first_update_id + 1


                elif first_chat_text == '2':
                    chatbot_bot.send_message(first_chat_id, 'servo 2 selezionato' + first_chat_name)
                    servoChoices = 2
                    new_offset = first_update_id + 1

                   
                elif first_chat_text == '3':
                    chatbot_bot.send_message(first_chat_id, 'servo 3 selezionato' + first_chat_name)
                    servoChoices = 3
                    new_offset = first_update_id + 1


                if servoChoices == 1:
                    chatbot_bot.send_message(first_chat_id, 'Inserisci quanto far girare il servo ' +first_chat_name)
                    new_offset = first_update_id + 1

                    if  first_chat_text == int:
                        #p.ChangeDutyCicle(int(first_chat_text))
                        chatbot_bot.send_message(first_chat_id, f'muovo di {int(first_chat_text)}' + first_chat_name)
                        new_offset = first_update_id + 1
                        servoChoices = -1

                if servoChoices == 2:
                    chatbot_bot.send_message(first_chat_id, 'Inserisci quanto far girare il servo ' +first_chat_name)
                    new_offset = first_update_id + 1

                    if  first_chat_text == int:
                        #p.ChangeDutyCicle(int(first_chat_text))
                        chatbot_bot.send_message(first_chat_id, f'muovo di {int(first_chat_text)}' + first_chat_name)
                        new_offset = first_update_id + 1
                        servoChoices = -1

                if servoChoices == 3:
                    chatbot_bot.send_message(first_chat_id, 'Inserisci quanto far girare il servo ' +first_chat_name)
                    new_offset = first_update_id + 1

                    if  first_chat_text == int:
                        #p.ChangeDutyCicle(int(first_chat_text))
                        chatbot_bot.send_message(first_chat_id, f'muovo di {int(first_chat_text)}' + first_chat_name)
                        new_offset = first_update_id + 1
                        servoChoices = -1



                else:
                    chatbot_bot.send_message(first_chat_id, 'Inserisci 1 per controllare il primo servo, \n 2 per il secondo, \n 3 per il terzo' + first_chat_name)
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()




        if type(int(first_chat_text)) == int:
                        #p.ChangeDutyCicle(int(first_chat_text))
                        chatbot_bot.send_message(first_chat_id, f"muovo di {int(first_chat_text)}" + first_chat_name)
                        new_offset = first_update_id + 1