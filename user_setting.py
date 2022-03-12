from batton import *
from telegram import ReplyKeyboardRemove
from datetime import datetime
from static_files import *
import time

def setting(update,context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    update.message.reply_html(text=user_setting_text.get(user[4]),reply_markup=setting_batton(user[4]))
    return 50

def setting_phone_number_update(update,context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    update.message.reply_html(text=update_phone_number_text.get(user[4]),reply_markup=phone_batton(user[4]))
    return 51

def get_phone_number_again_byuser(update, context):
    userID = update.effective_chat.id
    phone = update.message.contact.phone_number
    user_lang = database.get_user_by_id(userID)[4]
    database.update_user_phone_number(userID,phone)
    context.bot.send_message(chat_id=userID,
                             text=update_phone_number_succesfully_text.get(user_lang,'page not found'),
                             parse_mode="HTML",
                             reply_markup=back_batton(user_lang))
    return 10