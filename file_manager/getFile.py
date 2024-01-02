from file_manager.constant import document_options,user_data,national_events
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from menu import main_menu


async def send_download_link(bot, callback_query):
    user_id = callback_query.from_user.id
    state = user_data[user_id]["state"]
    language = user_data[user_id]["language"]
    festival = callback_query.data
 
    direct_download_link = f"https://shubhanshu74156.blob.core.windows.net/shubhanshu74156/{state}/{language}/{festival}.pdf"
    print (direct_download_link)
 
        # Send the direct download link as a message
    await bot.send_document(
        callback_query.message.chat.id,
       direct_download_link,
    )
    await main_menu(bot, callback_query.message)
async def send_event(bot, callback_query):
    for event_key, event_name in national_events.items():
        await bot.send_message(
            callback_query.message.chat.id,
            f"Upcoming {event_name} event!"
        )
    await main_menu(bot, callback_query.message)