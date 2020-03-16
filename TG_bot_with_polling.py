# бот для телеграм
# для получения информации о маркировке упаковки для раздельного сбора мусора

# -*- coding: utf-8 -*-

import telebot
import parser

token = '000000000:AAAAAaAA0Aaaaa0aaAaaAa0aAaAAaAaAaaa'
bot = telebot.TeleBot(token, threaded=False)
file = 'file_path'

while True:
    try:
        @bot.message_handler(commands=['start', 'go'])
        def start_handler(message):
            chat_id = message.chat.id
            text = message.text
            msg = bot.send_message(chat_id, 'Привет!\nВведите код маркировки или идентификатор '
                                            'упаковочного материала, чтобы узнать о его переработке.')
            bot.register_next_step_handler(msg, text_handler)

        def get_lables_from_file(file):
            lables = []
            with open(file, 'r') as file:
                data = file.read().splitlines()
                # делаем из списка переданных строк словарь, где значение - одна стринга
                for line in range(len(data)):
                    lables.append(data[line].split(':'))
                lables = dict(lables)
                
                # парсим созданный словарь, чтобы ключом была числовая маркировка без 0 (str),
                # а значением - список стрингов с вариантами этой же маркировки
                for key, value in lables.items():
                    lables[key] = value.split(';')
            return lables

        def recognize_lable(lable, file):
            requested_lable = lable.lower()
            recognized_from_text = get_lables_from_file(file)
            recognized = None
            
            for key, value in recognized_from_text.items():
                if requested_lable in value:
                    recognized = value[-1]
                    break
                else:
                    recognized = 'Упс... Кажется, такой маркировки нет в базе. Проверьте правильность ввода: например, 1, 01, PVC.'
            return recognized

        @bot.message_handler(content_types='text')
        def text_handler(message):
            text = message.text.lower()
            chat_id = message.chat.id
            recognized = recognize_lable(text, file)
            bot.send_message(chat_id, recognized)

        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
