# Import necessary libraries and modules
import logging
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from handlers.getAppealHandler import cb_handler
from menu import main_menu
from dotenv import load_dotenv
import os
import sys
import io
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import asyncio

# Set encoding for stdout to handle special characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Pyrogram client
bot = Client(
    "yeshbot",
    bot_token=os.getenv("BOT_TOKEN"),
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
)

# Define the target group ID
TARGET_GROUP_ID = -1002139412083 # demo group

# Define a function to check if a user is a member of the group
async def is_group_member(user_id):
    try:
        user = await bot.get_chat_member(TARGET_GROUP_ID, user_id) 
        return user
    except UserNotParticipant:
        return False

# Handle "/start" command for private messages
@bot.on_message(filters.command("start") & filters.private)
async def start_command_handler(client, message):
    user_id = message.from_user.id
    allowed = await is_group_member(user_id)

    # Check if the user is a group member
    if not allowed:
        # Send "Sorry" message if not a group member
        sorry_message = "Sorry, you must join our group to use this bot!"
        await message.reply(sorry_message)

        # Create an inline keyboard with a "Start" button
        start_button = InlineKeyboardButton("Start", callback_data="back")
        keyboard = InlineKeyboardMarkup([[start_button]])

        # Send the keyboard along with the "Sorry" message
        await message.reply("Click the 'Start' button to use the bot:", reply_markup=keyboard)
        return

    # If the user is a group member, display the main menu
    await main_menu(client, message)

# Define global variables for welcome message handling
members_name = []
last_welcome_time = None
welcome_sent = False
welcome_lock = asyncio.Lock()

# Handle new members joining the group
@bot.on_message(filters.group & filters.new_chat_members)
async def welcome(client, message):
    global members_name, last_welcome_time, welcome_sent

    # Check if a welcome message was sent within the last 3 seconds
    if last_welcome_time and (datetime.now() - last_welcome_time).total_seconds() < 3:
        return

    new_members = message.new_chat_members

    start_time = datetime.now()

    # Capture new members within the 3-second window
    while (datetime.now() - start_time).total_seconds() < 3:
        for member in new_members:
            
            # Exclude the bot itself from greeting
            if member.id == (await bot.get_me()).id:
                continue

            # Skip greeting other bots
            if member.is_bot:
                continue

            full_name = f"{member.first_name} {member.last_name}" if member.last_name else member.first_name
            if full_name not in members_name:
                members_name.append(full_name)

        await asyncio.sleep(1)

    # Print the list of new member names
    print(members_name)

    # If there are new members and a welcome message hasn't been sent
    async with welcome_lock:
        if len(members_name) > 0 and not welcome_sent:
            # Send a welcome message with new member names
            welcome_msg = f"Hi {', '.join(members_name)}! Welcome to the group! \n please click on this username to access the bot -  @yeshpal_bot "
            await bot.send_message(chat_id=message.chat.id, text=welcome_msg)
            members_name.clear()
            last_welcome_time = datetime.now()
            welcome_sent = True

    # Release the lock after sending the welcome message
    await asyncio.sleep(1)  # Reset the lock after 1 seconds
    welcome_sent = False

# Handle callback queries
@bot.on_callback_query()
async def handle_callback_query(client, callback_query):
    user_id = callback_query.from_user.id
    allowed = await is_group_member(user_id)
    if not allowed:
        # Send a message if the user is not a group member
        await callback_query.answer("You must join our member's only group to acess the features of this bot!") 
        return
    # Handle the callback query using the specified handler
    await cb_handler(client, callback_query)

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(bot.run())
