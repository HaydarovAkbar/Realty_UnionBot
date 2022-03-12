from batton import *
import time
database = Database()

def rek(update,context):
    user_id = update.message.chat.id
    user = database.get_user_by_id(user_id)
    context.bot.send_message(chat_id=user_id,
                             text=reklama_text.get(user[4]),
                             parse_mode="HTML",
                             reply_markup=back_batton(user[4]))
    return 150


def rek_video(update, context):
    text = update.message.caption
    video = update.message.video['file_id']
    user_id = update.message.chat.id
    if text is None:
        text = ''
    user = database.get_user_by_id(user_id)
    if video:
        s = 0
        for item in database.get_id():
                try:
                    context.bot.send_video(chat_id=item[0],
                                           video=video,
                                           caption=text + "\n\n    @Realtyunionbot",
                                           disable_notification=True)
                    time.sleep(0.05)

                    s += 1
                except Exception as e:
                    pass
        context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=back_batton(user[4]))
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Video jo'natishingiz kerak edi adashdingiz",
                                 reply_markup=back_batton(user[4]))
    return 100

def rek_photo(update, context):
    user_id = update.message.chat.id
    user = database.get_user_by_id(user_id)
    caption = update.message.caption
    if caption is None:
        caption = ''
    photo = update.message.photo[0]["file_id"]
    if photo:
        s = 0
        for item in database.get_id():
                try:
                    context.bot.send_photo(chat_id=item[0],
                                           photo=photo,
                                           caption=caption + "\n\n    @Realtyunionbot",
                                           disable_notification=True)
                    time.sleep(0.05)

                    s += 1
                except Exception as e:
                    print(e)
        context.bot.send_message(chat_id=user_id,
                                     text=f"jo'natgan  xabaringiz {s}-ta userga bordi!",
                                     reply_markup=back_batton(user[4]))
    else:
        context.bot.send_message(chat_id=user_id,
                                 text=f"Siz Rasm jo'natishingiz kerak edi adashdingiz!",
                                 reply_markup=back_batton(user[4]))
    return 100

def rek_text(update, context):
    user_id = update.message.chat.id
    user = database.get_user_by_id(user_id)
    text = update.message.text
    s = 0
    for item in database.get_id():
            try:
                context.bot.send_message(chat_id=item[0], text=text + "\n\n    @Realtyunionbot")
                time.sleep(0.05)
                s += 1
            except Exception as e:
                pass
    context.bot.send_message(chat_id=user_id,
                                 text=f"Jo'natgan  xabaringiz {s}-ta userga bordi!",
                                 reply_markup=back_batton(user[4]))
    return 100
