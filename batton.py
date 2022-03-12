from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton
from connect import Database
from static_files import *

database = Database()


language_batton = InlineKeyboardMarkup([
    [InlineKeyboardButton("🇺🇿 O'zbek tili (Lotin)",callback_data='uz_latn')],
    [InlineKeyboardButton("🇺🇿 Узбек тили (Криль)",callback_data='uz_cyrl'),],
    [InlineKeyboardButton("🇷🇺 Rus tili",callback_data='ru')]
])


def menyu_batton(lang='ru'):
    batton_data = menyu_text.get(lang)
    batton = ReplyKeyboardMarkup([
        [batton_data[0],batton_data[1]],
        [batton_data[2]],
        [batton_data[3]]
    ],resize_keyboard=True)
    return batton
def admin_basic_batton(lang='ru'):
    batton_data = admin_menyu_text.get(lang)
    batton = ReplyKeyboardMarkup([
        [batton_data[0],batton_data[1]],
        [batton_data[2],batton_data[3]],
        [batton_data[4]]
    ],resize_keyboard=True)
    return batton
def admin_menyu_batton(lang='ru'):
    batton_data = admin_basic_menyu_text.get(lang)
    batton = ReplyKeyboardMarkup([
        [batton_data[0],batton_data[1]],
        [batton_data[2],batton_data[3]],
        [batton_data[4], batton_data[5]],
        [batton_data[6],batton_data[7],],
        [batton_data[8],batton_data[9]]
    ],resize_keyboard=True)
    return batton

def phone_batton(til='uz_latn'):
    text = kontakt.get(til)
    phone = KeyboardButton(text,request_contact=True)
    contact_key = ReplyKeyboardMarkup([[phone]], resize_keyboard=True)
    return contact_key

def back_batton(lang='uz_latn'):
    text = back_batton_text.get(lang)
    batton = ReplyKeyboardMarkup([[text]],resize_keyboard=True)
    return batton

def service_batton(lang='uz_latn'):
    service_data = database.get_all_serviec()
    a,b = [],[]
    for item in service_data:
        if len(b) > 2:
            a.append(b)
            b = []
        if lang == 'uz_latn':
            b.append(InlineKeyboardButton(f"{item[1]}", callback_data=f'{item[0]}'))
        elif lang == 'uz_cyrl':
            b.append(InlineKeyboardButton(f"{item[5]}", callback_data=f'{item[0]}'))
        else:
            b.append(InlineKeyboardButton(f"{item[6]}", callback_data=f'{item[0]}'))
    a.append(b)
    return InlineKeyboardMarkup(a)

def picture_back_batton(lang='uz_latn'):
    back_text,confirmation_text = back_batton_text.get(lang),confirmation.get(lang)
    batton = ReplyKeyboardMarkup([[back_text],[confirmation_text]],resize_keyboard=True)
    return batton

def setting_batton(lang='uz_latn'):
    batton_data = user_setting_batton_text.get(lang)
    batton = ReplyKeyboardMarkup([
        [batton_data[0]],
        [batton_data[1]],
        [batton_data[2]]
    ],resize_keyboard=True)
    return batton
