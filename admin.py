from batton import *
from datetime import datetime
from static_files import *
from write_to_xls import xls_writer
from datetime import timedelta
admin_list = {}


def admin_basic_(update,context):
    userID = update.effective_chat.id
    user = database.get_user_by_id(userID)
    update.message.reply_html(text=admin_user_to_menyu_text.get(user[4]),reply_markup=admin_menyu_batton(user[4]))
    return 100

def get_all_user(update, context):
    userID = update.effective_chat.id
    user_lang = database.get_user_by_id(userID)[4]
    context.bot.send_message(chat_id=userID,
                             text=get_all_user_text.get(user_lang,'page not found'),
                             parse_mode="HTML",)
    all_user = database.get_user_50()
    all_text = "{:<2} || {:<10} || {:<23}\n\n".format("Number", "Name", "Username")
    for item in all_user:
        try:
            all_text += "{:<2}). || <b>{:<10}</b> || @{:<23}\n".format(item[0], item[1], item[2])
        except:
            pass
    context.bot.send_message(chat_id=userID,
                             text=all_text,
                             parse_mode="HTML",
                             reply_markup=back_batton(user_lang))
    return 100


def admin_lists(update, context):
    try:
        name = update.message.from_user.first_name
        admin_text = name + "ADMINS :)\n\n"
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        for i in database.get_admin():
            admin_text += f"{i[0]}. {i[1]}  @{i[4]}\n"
        context.bot.send_message(chat_id=userID, text=admin_text,parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 100

def get_new_admin_id(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        context.bot.send_message(chat_id=userID,
                                 text=insert_new_admin_id_text.get(user_lang),
                                 parse_mode="HTML",
                                 reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
    return 101


def get_new_adminID(update, context):
    try:
        global admin_list
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        admin_id = update.message.text
        if admin_id.isdigit():
            admin_list[userID] = int(admin_id)
            context.bot.send_message(chat_id=userID,
                                     text=insert_new_admin_username_text.get(user_lang),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user_lang))
            return 102
        else:
            context.bot.send_message(chat_id=userID,
                                     text=insert_new_admin_id_bag_text.get(user_lang),
                                     parse_mode="HTML",
                                     reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
        return 101


def get_new_admin_username(update, context):
    username = update.message.text
    userID = update.effective_chat.id
    try:
        user_lang = database.get_user_by_id(userID)[4]
        now = datetime.now() + timedelta(hours=5)
        now = now.strftime("%d.%m.%Y")
        A = database.add_admin(admin_list[userID],username,now)
        if A:
            context.bot.send_message(chat_id=userID, text=add_admin_succesfully_text.get(user_lang),parse_mode="HTML",reply_markup=back_batton(user_lang))
        else:
            context.bot.send_message(chat_id=userID, text=add_admin_bag_text.get(user_lang),parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=userID,
                                 text="Xatolik yuz berdi Dasturchi bilan bog'lanishni maslahat beraman!")
    return 100

def delete_admin_get_ID(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        context.bot.send_message(chat_id=userID, text=delete_admin_text.get(user_lang),
                                 parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 105

def delete_admin(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        adminID = update.message.text
        A = database.delete_admin(adminID)
        if A is True:
            context.bot.send_message(chat_id=userID, text=delete_admin_succesfully_text.get(user_lang),parse_mode="HTML",reply_markup=back_batton(user_lang))
        else:
            context.bot.send_message(chat_id=userID, text=A,reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 100

def get_application_(update, context):
    try:
        userID = update.effective_chat.id
        now = datetime.now() + timedelta(hours=5)
        now = now.strftime("%d.%m.%Y")
        data = database.get_today_app_(now)
        fullname,username,phone,language,job,service,address,parametr,condition,application_time = [],[],[],[],[],[],[],[],[],[]
        for item in data:
            user = database.get_user_by_id(item[8])
            fullname.append(user[1])
            username.append(user[2])
            phone.append(user[3])
            language.append(user[4])
            job.append(item[1])
            service.append(database.get_all_service_by_id(item[2])[1])
            address.append(item[3])
            parametr.append(item[4])
            condition.append(item[5])
            application_time.append(item[6])
        writer_data = {
            'fullname':fullname,
            'username':username,
            'phone': phone,
            'language': language,
            'job': job,
            'service': service,
            'address': address,
            'parametr': parametr,
            'condition': condition,
            'application_time': application_time,
        }
        xls_writer(writer_data)
        context.bot.send_document(chat_id=userID, document=open("application.xlsx","rb"), filename=f'{now}.xlsx')
    except Exception as e:
        print(e)
    return 100

def admin_create_service_get_name(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        context.bot.send_message(chat_id=userID, text=get_service_name_from_admin_text.get(user_lang),
                                 parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 110

def admin_create_service(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        service_name = update.message.text
        if not ',' in service_name:
            context.bot.send_message(chat_id=userID, text=get_service_name_from_admin_BAG_text.get(user_lang),
                                     parse_mode="HTML", reply_markup=back_batton(user_lang))
            return 110
        now = datetime.now() + timedelta(hours=5)
        now = now.strftime("%d.%m.%Y")
        uz_latn,uz_cyrl,ru = service_name.split(',')
        A = database.add_service(uz_latn,uz_cyrl,ru,userID,now)
        if A:
            context.bot.send_message(chat_id=userID, text=add_service_succesfully_text.get(user_lang),
                                 parse_mode="HTML",reply_markup=back_batton(user_lang))
        else:
            context.bot.send_message(chat_id=userID, text=add_service_succesfully_BAG_text.get(user_lang),
                                 parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 100

def admin_delete_service_get_name(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        context.bot.send_message(chat_id=userID, text=delete_service_text.get(user_lang),
                                 parse_mode="HTML",reply_markup=service_batton(user_lang))
        context.bot.send_message(chat_id=userID, text=delete_service_or_back_text.get(user_lang),
                                 parse_mode="HTML", reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 111

def delete_user_service(update,context):
    try:
        userID= update.effective_chat.id
        query = update.callback_query
        user = database.get_user_by_id(userID)
        database.delete_service(query.data)
        query.delete_message(timeout=1)
        context.bot.send_message(chat_id=userID,text=delete_service_succesfully_text.get(user[4]),
                                 parse_mode="HTML",reply_markup=back_batton(user[4]))
    except Exception as e:
        print(e)
    return 100

def bot_stats(update, context):
    try:
        userID = update.effective_chat.id
        user_lang = database.get_user_by_id(userID)[4]
        user_count = database.get_all_user_COUNT()[0]
        admin_count = database.get_all_admin_COUNT()[0]
        application_count = database.get_all_application_COUNT()[0]
        service_count = database.get_all_serviec_COUNT()[0]
        now = datetime.now() + timedelta(hours=5)
        now = now.strftime("%d.%m.%Y %H:%M")
        if user_lang =='uz_latn':
            text = f"""
<b>Realty Union Bot</b>  <code>Sana: {now}</code> 

👨‍👨‍👧‍👦 Foydalanuvchilar soni: {user_count}

👮‍♂️ Adminlar soni: {admin_count}

🗂 Arizalar soni: {application_count}

⚖️ Barcha xizmat turlar soni: {service_count}

🤖<b> LINK:</b> @Realtyunionbot
"""
        elif user_lang == 'uz_cyrl':
            text = f"""
<b>Бот Realty Union</b> <code>Сана: {now}</code>

👨‍👨‍👧‍👦 Фойдаланувчилар сони: {user_count}

👮‍♂️ Администратор Сони: {admin_count}

🗂 Аризалар Сони: {application_count}

⚖️ Барча хизмат турлар сони: {service_count}

🤖<b>СЫЛКА:</b> @Realtyunionbot
            """
        else:
            text = f"""
<b> Бот Realty Union </b> <code> Дата: {now} </code>

👨‍👨‍👧‍👦 Количество пользователей: {user_count}

👮‍♂️ Количество админов: {admin_count}

🗂 Количество приложений: {application_count}

⚖️ Количество всех типов услуг: {service_count}

🤖 <b> ССЫЛКА: </b> @Realtyunionbot
            """
        context.bot.send_message(chat_id=userID, text=text,
                                 parse_mode="HTML",reply_markup=back_batton(user_lang))
    except Exception as e:
        print(e)
    return 100

