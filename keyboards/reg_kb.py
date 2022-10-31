from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('ПЭИ-19')
b2 = KeyboardButton('ПИЭ-21')
b3 = KeyboardButton('Кнопка 3')

#resize_keyboard изменяется размер по названию
#one_time_keyboard клавиатура скрывается после использования
reg_kb = ReplyKeyboardMarkup(resize_keyboard=True,)

#.row() всё в строку
#.add() по строкам
#.insert()
reg_kb.row(b1,b2,b3)