from batton import *
from static_files import *

user_data = {}

def start(update, context):
    lang = update.message.from_user.language_code
    update.message.reply_html(text=text1.get(lang,text1['uz_cyrl']), reply_markup=language_batton)
    return 1

def get_language_byuser(update, context):
    global user_data
    query = update.callback_query
    user_lang = query.data
    query.delete_message(timeout=1)
    userID = update.effective_chat.id
    user_data[userID] = {'lang':user_lang}
    database_user = database.get_user_by_id(userID)
    if database_user:
        a = database.update_user_language(userID,user_lang)
        # admin kirishlari uchun
        if database.get_one_admin(userID):
            context.bot.send_message(chat_id=userID, text=admin_user_to_menyu_text.get(user_lang, '.'), parse_mode="HTML",
                                     reply_markup=admin_basic_batton(user_lang))
            return 10
        context.bot.send_message(chat_id=userID, text=again_start_user_bot.get(user_lang,'.'),parse_mode="HTML",reply_markup=menyu_batton(user_lang))
        return 10
    context.bot.send_message(chat_id=userID,
                             text=get_phone_number_text.get(user_lang),
                             parse_mode="HTML",
                             reply_markup=phone_batton(user_lang))
    return 2

def get_phone_number_byuser(update, context):
    user = update.message.from_user
    userID = update.effective_chat.id
    phone,user_lang = update.message.contact.phone_number,user_data[userID]['lang']
    database.add_user_to_database(user_lang,phone,user.first_name,userID,user.username)
    context.bot.send_message(chat_id=userID,
                             text=sign_up_user_text.get(user_lang,'page not found'),
                             parse_mode="HTML",
                             reply_markup=menyu_batton(user_lang))
    return 10

def back(update, context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    if database.get_one_admin(userID):
        context.bot.send_message(chat_id=userID, text=admin_user_to_menyu_text.get(user[4], '.'), parse_mode="HTML",
                                 reply_markup=admin_basic_batton(user[4]))
        return 10
    context.bot.send_message(chat_id=userID,
                             text=back_user_text.get(user[4],'page not found'),
                             parse_mode="HTML",
                             reply_markup=menyu_batton(user[4]))
    return 10

def reference_by_organization(update, context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    context.bot.send_message(chat_id=userID,
                             text=about_organization_text.get(user[4],"Page not found"),
                             parse_mode="HTML",
                             reply_markup=back_batton(user[4]))
    return 10

def communication_by_organization(update, context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    context.bot.send_message(chat_id=userID,
                             text=communication_organization_text.get(user[4],"Page not found"),
                             parse_mode="HTML",
                             reply_markup=back_batton(user[4]))
    context.bot.send_location(chat_id=userID,longitude=longitude,latitude=latitude)
    return 10


def fallback(update, context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    context.bot.send_message(chat_id=userID,
                             text=back_user_text.get(user[4],'page not found'),
                             parse_mode="HTML",
                             reply_markup=menyu_batton(user[4]))
    return 10

def help(update, context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    context.bot.send_message(chat_id=userID,
                             text=help_text.get(user[4],'page not found'),
                             parse_mode="HTML",
                             reply_markup=back_batton(user[4]))
    return 10
