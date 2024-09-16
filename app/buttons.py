from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Buttons: 
    menu_button = ReplyKeyboardMarkup(
        keyboard=[
        [KeyboardButton(text='1 choose'), KeyboardButton(text='2 choose')]
        [KeyboardButton(text='3 choose')]
    ],
        resize_keyboard=True, input_field_placeholder='Выберите пунт меню.')
    

    info_button = ReplyKeyboardMarkup(
        keyboard=[
        [KeyboardButton(text='В меню🧑🏿‍💻🗂')]
    ],
        resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')
    

    order_button = ReplyKeyboardMarkup(
        keyboard=[
        KeyboardButton(text='2 choose'), KeyboardButton(text='1 choose')
    ], 
        resize_keyboard=True)


    payment_button = ReplyKeyboardMarkup(
        keyboard=[
        KeyboardButton(text='1 choose'), KeyboardButton(text='2 choose')
    ], 
        resize_keyboard=True)