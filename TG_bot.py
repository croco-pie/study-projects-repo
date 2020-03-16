# бот для телеграм для получения информации о маркировке упаковки для раздельного сбора мусора
# пробная версия без опроса сервера, некоторых важных проверок и подключения сторонних библиотек
# функции импортировать из TG_bot_funcs (тоже оставляю на память)

# оставляю на память

import TG_bot_funcs as tgbot

token = 'token'
bot_url = 'https://api.telegram.org/bot%s/' % token
file_output = 'file_path'


last_upd = tgbot.get_last_update(tgbot.get_updates_json(bot_url))

last_text = tgbot.get_last_text(last_upd)


if last_text == '/start':
    print('Введите код маркировки или идентификатор упаковочного материала, чтобы узнать о его переработке.')
else:
    lables = tgbot.get_lable_from_file('file_path', parse_dict = True)
    recognized = tgbot.recognize_lable(last_text, lables)

tgbot.get_recycling_info(recognized)

chat_id = tgbot.get_chat_id(last_upd)
tgbot.send_message(chat_id, recognized)
   




