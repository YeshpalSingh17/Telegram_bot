
from menu import state_menu,festivals_menu,language_menu,Upcoming_event_menu,main_menu,show_event_state,handel_state_event
from file_manager.getFile import send_download_link,send_event
from buttons import EVENT_STATE_BUTTONS,MAIN_MENU_BUTTONS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def cb_handler(bot, callback_query):
    
    if callback_query.data == "Get festivals doc":
        await state_menu(callback_query)

    elif callback_query.data == "Upcoming event":
        await Upcoming_event_menu(callback_query)

    elif callback_query.data in ["Chhattisgarh", "Maharashtra","Uttarpradesh"]:
        await language_menu(callback_query)

    elif callback_query.data in ["English","Hindi","Marathi"]:
        await festivals_menu(callback_query)

    elif callback_query.data in ["diwali", "holi", "christmas", "dusherra"]:
        await send_download_link(bot, callback_query)

    elif callback_query.data == "National":
       await send_event(bot, callback_query)

    elif callback_query.data == "State":
       await show_event_state(callback_query)

    elif callback_query.data in ["State1","State2","State10","State3","State4","State5"]:
        await handel_state_event(bot, callback_query)

    elif callback_query.data == "get_payment_QR":
        await bot.send_photo(callback_query.from_user.id, "https://media.istockphoto.com/id/1251133771/photo/hand-using-mobile-smart-phone-scan-qr-code-on-blue-background-cashless-technology-and-digital.jpg?s=2048x2048&w=is&k=20&c=J1x-OhpxAWp9V-k1jsYKpJEx-EY-wMUB9AoYEnLRHD0=")
        await main_menu(bot, callback_query.message)

    elif callback_query.data == "calander":
        await bot.send_document(
            chat_id=callback_query.from_user.id,
            document="https://www.vertex42.com/calendars/pdfs/2023-yearly-holiday-calendar.pdf",
        )
        await main_menu(bot, callback_query.message)

    elif callback_query.data == "back":
        await main_menu(bot, callback_query.message)

    else:
        await cb_handler(client, callback_query)