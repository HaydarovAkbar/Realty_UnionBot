from telegram.ext import Updater,ConversationHandler
from telegram.ext import Dispatcher
from telegram.ext import CommandHandler,CallbackQueryHandler,MessageHandler,Filters
from methods import *
from bot_service import *
from user_setting import *
from admin import *
from rek import *

update = Updater(TOKEN,use_context=True,workers=1000) # ,use_context=True,workers=1000
dispatcher = update.dispatcher
handler = ConversationHandler(
    entry_points=[CommandHandler('start',start),
                    CommandHandler('help',help),
                  MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[0] + ')$'), get_full_name_to_ask),
                  MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[1] + ')$'), reference_by_organization),
                  MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[2] + ')$'), communication_by_organization),
                  MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[3] + ')$'), setting),
                  MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[4] + ')$'), admin_basic_),

                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[0] + ')$'), get_full_name_to_ask),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[1] + ')$'),
                                    reference_by_organization),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[2] + ')$'),
                                    communication_by_organization),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[3] + ')$'), setting),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[4] + ')$'), admin_basic_),

                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[0] + ')$'), get_full_name_to_ask),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[1] + ')$'),
                                    reference_by_organization),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[2] + ')$'),
                                    communication_by_organization),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[3] + ')$'), setting),
                     MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[4] + ')$'), admin_basic_),

                     MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
                  MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
                  MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
                  ],
    states={
        1:[CommandHandler('start',start),
           CommandHandler('help',help),
            CallbackQueryHandler(get_language_byuser)],
        2:[CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.contact, get_phone_number_byuser)],
        10:[CommandHandler('start',start),
            CommandHandler('help',help),
           MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[0] + ')$'), get_full_name_to_ask),
           MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[1] + ')$'), reference_by_organization),
           MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[2] + ')$'), communication_by_organization),
           MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[3] + ')$'), setting),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_latn')[4] + ')$'), admin_basic_),

            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[0] + ')$'), get_full_name_to_ask),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[1] + ')$'),
                           reference_by_organization),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[2] + ')$'),
                           communication_by_organization),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[3] + ')$'), setting),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('uz_cyrl')[4] + ')$'), admin_basic_),

            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[0] + ')$'), get_full_name_to_ask),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[1] + ')$'),
                           reference_by_organization),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[2] + ')$'),
                           communication_by_organization),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[3] + ')$'), setting),
            MessageHandler(Filters.regex('^(' + admin_menyu_text.get('ru')[4] + ')$'), admin_basic_),

            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
           MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
           MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.location,back )
        ],
        30 : [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_user_full_name),
        ],
        31: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_user_job),

        ],
        32: [CommandHandler('start',start),
            CommandHandler('help',help),
            CallbackQueryHandler(get_user_service),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        ],
        33:[CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_user_addres),
        ],
        34: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_user_situation),

        ],
        35: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.photo, get_user_object_picture),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        ],
        36: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + confirmation.get('uz_latn') + ')$'), send_user_time_txt),
            MessageHandler(Filters.regex('^(' + confirmation.get('uz_cyrl') + ')$'), send_user_time_txt),
            MessageHandler(Filters.regex('^(' + confirmation.get('ru') + ')$'), send_user_time_txt),

            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.photo, get_user_object_again_picture),
        ],
        37: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + confirmation.get('uz_latn') + ')$'), confirmation_user_service),
            MessageHandler(Filters.regex('^(' + confirmation.get('uz_cyrl') + ')$'), confirmation_user_service),
            MessageHandler(Filters.regex('^(' + confirmation.get('ru') + ')$'), confirmation_user_service),

            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        ],
        38: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_user_time),
        ],
        39: [CommandHandler('start',start),
            CommandHandler('help',help),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
            MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
            MessageHandler(Filters.text, get_object_size_from_user),

        ],
    50: [CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_latn')[0] + ')$'), start),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_latn')[1] + ')$'), setting_phone_number_update),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_latn')[2] + ')$'), back),

        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_cyrl')[0] + ')$'), start),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_cyrl')[1] + ')$'),
                       setting_phone_number_update),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('uz_cyrl')[2] + ')$'), back),

        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('ru')[0] + ')$'), start),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('ru')[1] + ')$'),
                       setting_phone_number_update),
        MessageHandler(Filters.regex('^(' + user_setting_batton_text.get('ru')[2] + ')$'), back),
    ],
    51: [CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.contact, get_phone_number_again_byuser)],

    100:[CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),

           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[0] + ')$'), get_all_user),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[1] + ')$'), admin_lists),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[2] + ')$'), get_new_admin_id),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[3] + ')$'), delete_admin_get_ID),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[4] + ')$'), get_application_),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[5] + ')$'),admin_create_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[6] + ')$'), admin_delete_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[7] + ')$'),bot_stats),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[8] + ')$'), rek),
            MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_latn')[9] + ')$'), back),

         MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[0] + ')$'), get_all_user),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[1] + ')$'),admin_lists),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[2] + ')$'),get_new_admin_id),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[3] + ')$'), delete_admin_get_ID),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[4] + ')$'),get_application_),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[5] + ')$'),admin_create_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[6] + ')$'), admin_delete_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[7] + ')$'), bot_stats),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[8] + ')$'), rek),
         MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('uz_cyrl')[9] + ')$'), back),

         MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[0] + ')$'), get_all_user),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[1] + ')$'),admin_lists),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[2] + ')$'),get_new_admin_id),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[3] + ')$'), delete_admin_get_ID),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[4] + ')$'), get_application_),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[5] + ')$'), admin_create_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[6] + ')$'), admin_delete_service_get_name),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[7] + ')$'), bot_stats),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[8] + ')$'), rek),
           MessageHandler(Filters.regex('^(' + admin_basic_menyu_text.get('ru')[9] + ')$'), back),

         ],
    101: [CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        MessageHandler(Filters.text, get_new_adminID)],
    102: [CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        MessageHandler(Filters.text, get_new_admin_username)],

    105: [CommandHandler('start',start),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        MessageHandler(Filters.text, delete_admin)],
    110: [CommandHandler('start',start),
        CommandHandler('help',help),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
        MessageHandler(Filters.text, admin_create_service)],
    111: [CommandHandler('start',start),
        CommandHandler('help',help),
        CallbackQueryHandler(delete_user_service),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
        MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
    ],
    150: [CommandHandler('start', start),
          CommandHandler('help', help),
          MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_latn') + ')$'), back),
          MessageHandler(Filters.regex('^(' + back_batton_text.get('uz_cyrl') + ')$'), back),
          MessageHandler(Filters.regex('^(' + back_batton_text.get('ru') + ')$'), back),
MessageHandler(Filters.text, rek_text),
MessageHandler(Filters.photo, rek_photo),
MessageHandler(Filters.video, rek_video),
          ],
},
    fallbacks=[MessageHandler(Filters.location, fallback),
                  CommandHandler('start',start)],
    run_async=True)
# dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(handler)
update.start_polling()
print("started polling")
# update.idle()

