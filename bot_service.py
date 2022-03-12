from batton import *
from telegram import ReplyKeyboardRemove
from datetime import datetime
from static_files import *
import time
from datetime import timedelta


aplication_data = {}
def get_full_name_to_ask(update,context):
    try:
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text = get_user_full_name_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        pass
    return 30

def get_user_full_name(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        user_full_name = update.message.text
        if not " " in user_full_name and not len(user_full_name) > 1:
            context.bot.send_message(chat_id=userID,
                                     text=get_user_full_name_bag_text.get(user[4]),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user[4]))
            return 30
        aplication_data[userID] = {'fullname':user_full_name}
        database.update_user_fullname(userID,user_full_name)
        context.bot.send_message(chat_id=userID,
                                 text = get_user_job_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        pass
    return 31

def get_user_job(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        user_job = update.message.text
        if not len(user_job) > 1:
            context.bot.send_message(chat_id=userID,
                                     text=get_user_full_name_bag_text.get(user[4]),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user[4]))
            return 31
        aplication_data[userID]['job'] = user_job
        context.bot.send_message(chat_id=userID,
                                 text = get_user_service_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=service_batton(user[4]))
    except Exception as e:
        pass
    return 32

def get_user_service(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        query = update.callback_query
        user = database.get_user_by_id(userID)
        aplication_data[userID]['service'] = query.data
        query.delete_message(timeout=1)
        context.bot.send_message(chat_id=userID,text=get_addres_text.get(user[4]),parse_mode="HTML",reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)
    return 33

def get_user_addres(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        addres = update.message.text
        if not " " in addres and not len(addres) > 1:
            context.bot.send_message(chat_id=userID,
                                     text=get_user_addres_bag_text.get(user[4]),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user[4]))
            return 33
        aplication_data[userID]['addres'] = addres
        context.bot.send_message(chat_id=userID,
                                 text = get_object_size_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        pass
    return 39
def get_object_size_from_user(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        size = update.message.text
        if not " " in size and not len(size) > 1:
            context.bot.send_message(chat_id=userID,
                                     text=get_object_size_bag_text.get(user[4]),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user[4]))
            return 39
        aplication_data[userID]['parametr'] = size
        context.bot.send_message(chat_id=userID,
                                 text = get_object_situation_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        pass
    return 34
def get_user_situation(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        situation = update.message.text
        if not len(situation) > 1:
            context.bot.send_message(chat_id=userID,
                                     text=get_object_situation_bag_text.get(user[4]),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user[4]))
            return 34
        aplication_data[userID]['situation'] = situation
        context.bot.send_message(chat_id=userID,
                                 text = get_object_pictures_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)
    return 35

def get_user_object_picture(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        photo = update.message.photo[-1]
        aplication_data[userID]['photo'] = [photo['file_id']]
        context.bot.send_message(chat_id=userID,
                                 text = get_object_pictures_again_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=picture_back_batton(user[4]))
    except Exception as e:
        print(e)
    return 36

def get_user_object_again_picture(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        photo = update.message.photo[-1]
        photo_list = aplication_data[userID]['photo']
        photo_list.append(photo['file_id'])
        aplication_data[userID]['photo'] = photo_list
        context.bot.send_message(chat_id=userID,
                                 text = get_object_pictures_again_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=picture_back_batton(user[4]))
    except Exception as e:
        print(e)
    return 36
def send_user_time_txt(update,context):
    try:
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        context.bot.send_message(chat_id=userID,
                                 text = get_user_time_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)
    return 38
def get_user_time(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        user_time = update.message.text
        aplication_data[userID]['time'] = user_time
        context.bot.send_message(chat_id=userID,
                                 text = user_confirmation_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=picture_back_batton(user[4]))
    except Exception as e:
        print(e)
    return 37

def confirmation_user_service(update,context):
    try:
        global aplication_data
        userID= update.effective_chat.id
        user = database.get_user_by_id(userID)
        u_a_d = aplication_data[userID] # user_app_data
        now = datetime.now() + timedelta(hours=5)
        created_date = now.strftime("%d.%m.%Y %H:%M")
        job, service_type, adress, parametr, condition, application_time, created_date, userid = u_a_d['job'],u_a_d['service'],u_a_d['addres'],u_a_d['parametr'],u_a_d['situation'],u_a_d['time'],created_date,userID,
        app_id = database.insert_application_data(job, service_type, adress, parametr, condition, application_time, created_date, userid)
        for url in u_a_d['photo']:
            database.add_photo_to_database(url,app_id[0])
            context.bot.send_photo(chat_id=-1001730966225,photo=url,caption=f"Murojat ID: {app_id[0]}")
        a = context.bot.send_sticker(chat_id=userID,
                                     sticker=sticer_url1)
        time.sleep(2)
        context.bot.delete_message(
            timeout=1,
            chat_id=(a.chat.id),
            message_id=int(a.message_id))
        context.bot.send_message(chat_id=userID,
                                 text = user_confirmation_and_text.get(user[4]),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)
    return 10
