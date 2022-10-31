from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Кнопка 1')
b2 = KeyboardButton('Кнопка 2')
b3 = KeyboardButton('Кнопка 3')

#resize_keyboard изменяется размер по названию
#one_time_keyboard клавиатура скрывается после использования
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#.row() всё в строку
#.add() по строкам
#.insert()
kb_client.row(b1,b2,b3)