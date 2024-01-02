from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from buttons import STATE_BUTTONS,MAIN_MENU_BUTTONS,FESTIVAL_BUTTONS,UPCOMING_EVENT_BUTTONS,LANGUAGE_BUTTONS,EVENT_STATE_BUTTONS
from file_manager.constant import user_data,state_events
from pyrogram import enums

async def state_menu(callback_query):
    await callback_query.message.edit_text(
        "Select state:",
        reply_markup=InlineKeyboardMarkup(STATE_BUTTONS),
        disable_web_page_preview=True
    )

async def language_menu(callback_query):
    user_id = callback_query.from_user.id
    user_data[user_id] = {"state": callback_query.data}
    await callback_query.message.edit_text(
        "Select language:",
        reply_markup=InlineKeyboardMarkup(LANGUAGE_BUTTONS),
        disable_web_page_preview=True
    )

async def festivals_menu(callback_query):
    user_id = callback_query.from_user.id
    user_data[user_id]["language"] = callback_query.data
    state = user_data[user_id]["state"]
    await callback_query.message.edit_text(
        "Select festivals:",
        reply_markup=InlineKeyboardMarkup(FESTIVAL_BUTTONS),
        disable_web_page_preview=True
    )

async def main_menu(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name}, I am a Pyrogram Bot.",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(MAIN_MENU_BUTTONS),
    )


async def Upcoming_event_menu(callback_query):
    await callback_query.message.edit_text(
            "add help message for users",
            reply_markup=InlineKeyboardMarkup(UPCOMING_EVENT_BUTTONS),
            disable_web_page_preview=True
        )

# async def back_menu(callback_query):
#     await callback_query.message.edit_text(
#         f"Hello {callback_query.from_user.first_name}, I am a Pyrogram Bot.",
#         disable_web_page_preview=True,
#         reply_markup=InlineKeyboardMarkup(MAIN_MENU_BUTTONS)
#     )

async def show_event_state(callback_query):
    await callback_query.message.edit_text(
        "Choose a state:",
        reply_markup=InlineKeyboardMarkup(EVENT_STATE_BUTTONS),
        disable_web_page_preview=True,
    )

async def handel_state_event(bot, callback_query):
    state = callback_query.data  # Extract the state from callback_data
    if state in state_events:
        events = state_events[state]
        message_text = "<b>Events List:</b>\n\n"
        for event in events:
            message_text += (
                f"<b>Event:</b> <u>{event['name']}</u>\n"
                f"<i>Description:</i> {event['description']}\n"
                f"<i>Location:</i> {event['location']}\n\n"
                f"<a href=\"https://example.com\">More Info</a>\n\n"
            )

        await bot.send_message(
            callback_query.message.chat.id,
            message_text,
            parse_mode=enums.ParseMode.HTML
            
        )
    await main_menu(bot, callback_query.message)
        
