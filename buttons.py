from pyrogram.types import InlineKeyboardButton

STATE_BUTTONS= [
            [InlineKeyboardButton("Chhattisgarh", callback_data='Chhattisgarh')],
            [InlineKeyboardButton("Maharastra", callback_data='Maharashtra')],
            [InlineKeyboardButton("Uttarpradesh", callback_data='Uttarpradesh')],
            [InlineKeyboardButton("Main menu", callback_data='back')],
        ]

MAIN_MENU_BUTTONS =  [
        InlineKeyboardButton("Get festivals doc", callback_data='Get festivals doc'),
        InlineKeyboardButton("Upcoming event", callback_data='Upcoming event')
    ],[
        InlineKeyboardButton("Get yearly calendar pdf", callback_data='calander'),
        InlineKeyboardButton("Get payment QR", callback_data='get_payment_QR'),
    ],[   
        InlineKeyboardButton("New joiner Form", callback_data='New joiner Form'),
        InlineKeyboardButton("Enable Notifier", callback_data='Enable Notifier')
    ]

UPCOMING_EVENT_BUTTONS= [
            [InlineKeyboardButton("National", callback_data='National')],
            [InlineKeyboardButton("State", callback_data='State')],
            [InlineKeyboardButton("Main menu", callback_data='back')],
        ]

LANGUAGE_BUTTONS = [
            [InlineKeyboardButton("English", callback_data='English')],
            [InlineKeyboardButton("Hindi", callback_data='Hindi')],
            [InlineKeyboardButton("Marathi", callback_data='Marathi')],
            [InlineKeyboardButton("Main menu", callback_data='back')],

        ]

FESTIVAL_BUTTONS=[
            [InlineKeyboardButton("Diwali", callback_data='diwali'),
            InlineKeyboardButton("Holi", callback_data='holi')],
            [InlineKeyboardButton("Christmas", callback_data='christmas'),
            InlineKeyboardButton("Dushera", callback_data='dusherra')],
            [InlineKeyboardButton("Main menu", callback_data='back')],
        ]

EVENT_STATE_BUTTONS = [
    [
        InlineKeyboardButton("Chhattisgrah", callback_data='State1'),
        InlineKeyboardButton("Maharastra", callback_data='State2')
    ],
    [
        InlineKeyboardButton("Delhi", callback_data='State10'),
        InlineKeyboardButton("Lucknow", callback_data='State3')
    ],
    [
        InlineKeyboardButton("Pune", callback_data='State4'),
        InlineKeyboardButton("Mumbai", callback_data='State5')
    ],
    [InlineKeyboardButton("Main menu", callback_data="back")]
]
