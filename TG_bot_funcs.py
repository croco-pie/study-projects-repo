# бот для телеграм - библиотека функций

import requests
import time

token = 'token'
bot_url = 'https://api.telegram.org/bot%s/' % token
file_output = 'file_path'

def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def get_last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_last_text(last_update):
    text = last_update['message']['text']
    return text

'''
-- решила не выносить этот кусок кода в функцию, вынесла в исполняемый файл в блок условия

def greet(last_text):
    try:
        if get_last_text(last_text) == '/start': # and last_text['message']['entities'][0]['type'] == 'bot_command':
            print('Привет!\nВведите код маркировки или идентификатор упаковочного материала, чтобы узнать о его переработке.')
    except TypeError:
        pass
'''

def greet():
    text = 'Привет!\nВведите код маркировки или идентификатор упаковочного материала, чтобы узнать о его переработке.'
    return text


def get_lable_from_file(file, parse_dict = False):
    lables = []
    with open(file, 'r') as file:
        data = file.read().splitlines()
        
        # делаем из списка переданных строк словарь, чтобы потом его парсить в нормальный вид
        for line in range(len(data)):
            lables.append(data[line].split(':'))
        lables = dict(lables)
        
        # парсим созданный словарь, чтобы ключом была числовая маркировка без 0 (str), 
        # а значением - список стрингов в вариантами этой же маркировки
        if parse_dict == True:
            for key, value in lables.items():
                lables[key] = value.split(',')
        return lables
  

def recognize_lable(text, lables):
    requested_lable = text.upper()
    is_in_lables = 'Упс... Кажется, такой маркировки нет в базе. Проверьте правильность ввода: например, 1, 01, PVC.'
    for key, value in lables.items():
        for lable in value:
            if requested_lable in value:
                is_in_lables = key
                break
    return is_in_lables
    
def get_chat_id(data):  
    chat_id = data['message']['chat']['id']
    return chat_id
    
def send_message(chat_id, text):  
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(bot_url + 'sendMessage', data=params)
    print(response)
    return response

def get_recycling_info(lable_to_get):
    lable = get_lable_from_file(file_output)
    for key, value in lable.items():
        if key == lable_to_get:
            print(value)

