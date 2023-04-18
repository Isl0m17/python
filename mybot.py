import telebot
from telebot import types

bot = telebot.TeleBot("6238394380:AAG3WwGvOBnWVoNj3b7YBM28I7yxORjzpAo")

# Вызов start через /start
@bot.message_handler(commands=['start'])
def start_menu(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📖 IT-Run", callback_data="run")
    key.add(btn1)
    text0 = "Hi 👋"
    bot.send_message(chat_id=msg.chat.id, text=text0, reply_markup=key)

# Вызов Quotes через /quotes
@bot.message_handler(commands=['run'])
def run(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Python', callback_data='python')
    btn2 = types.InlineKeyboardButton(text='💘 Turtle', callback_data='turtle')
    btn3 = types.InlineKeyboardButton(text='💯 Pygame', callback_data='pygame')
    btn4 = types.InlineKeyboardButton(text='🔋 Telebot', callback_data='telebot')
    btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1')
    key.add(btn1,btn2)
    key.add(btn3,btn4)
    key.add(btn0)
    text1 = 'Choose the category of 📖 Themes:'
    bot.send_message(chat_id=msg.chat.id, text=text1, reply_markup=key)

# Вызов help через /help
@bot.message_handler(commands=['help'])
def help(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_2')
    key.add(btn0)
    text1_0 = '⚫ Cho zdes ne ponatno Blet!\n⚫ Click on 📖 Quotes button in main menu'
    bot.send_message(chat_id=msg.chat.id, text=text1_0, reply_markup=key)

# Вызов about через /about
@bot.message_handler(commands=['about'])
def about(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_3')
    key.add(btn0)
    text1_1 = '⚫ This bot is a child of a student.Who learns programming in TJK-Dushanbe.\n'
    text1_2 = "⚫ It's simple bot where you can find quotes for your heart."
    text1_3 = text1_1 + text1_2
    bot.send_message(chat_id=msg.chat.id, text=text1_3, reply_markup=key)

# Вызов language через /lang
@bot.message_handler(commands=['lang'])
def language(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='🇬🇧 English', callback_data='eng')
    btn2 = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='rus')
    btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_4')
    key.add(btn1)
    key.add(btn2)
    key.add(btn0)
    text_1 = 'This stage is under development ⚙️...\nStay tuned for future updates!'
    bot.send_message(chat_id=msg.chat.id, text=text_1, reply_markup=key)

# Вызов всех других функций
@bot.callback_query_handler(func=lambda call: True)
def all_functions(call: types.CallbackQuery):
    # Keyboards - start
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📖 IT-Run", callback_data="run")
    key.add(btn1)
    # Return to the main menu
    key2 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📖 Quotes", callback_data="quotes")
    btn2 = types.InlineKeyboardButton("💡 Help", callback_data="help")
    btn3 = types.InlineKeyboardButton("📜 About Bot", callback_data="about")
    btn4 = types.InlineKeyboardButton("🏳️ Language", callback_data="lang")
    key2.add(btn1)
    key2.add(btn2)
    key2.add(btn3)
    key2.add(btn4)
    # Return to category of themes
    key3 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='💲 Business', callback_data='buss')
    btn2 = types.InlineKeyboardButton(text='💘 Love', callback_data='love')
    btn3 = types.InlineKeyboardButton(text='💯 Friendship', callback_data='friend')
    btn4 = types.InlineKeyboardButton(text='🔋 Motivation', callback_data='motiv')
    btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1')
    key3.add(btn1,btn2)
    key3.add(btn3,btn4)
    key3.add(btn0)

    # Вызов Quotes   
    if call.data == "run":
        text1 = 'Choose the category of 📖 Themes:'
        key = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Python', callback_data='python')
        btn2 = types.InlineKeyboardButton(text='💘 Turtle', callback_data='turtle')
        btn3 = types.InlineKeyboardButton(text='💯 Pygame', callback_data='pygame')
        btn4 = types.InlineKeyboardButton(text='🔋 Telebot', callback_data='telebot')
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1')
        key.add(btn1,btn2)
        key.add(btn3,btn4)
        key.add(btn0)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1, reply_markup=key)

    # Категория Business
    elif call.data == 'python':
        global text2
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1.1')
        key.add(btn0)
        text2 = text2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text2, reply_markup=key)

    # Категория Love
    elif call.data == 'love':
        global text3
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1.2')
        key.add(btn0)
        text3 = text3
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text3, reply_markup=key)

    # Категория Friendship
    elif call.data == 'friend':
        global text4
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1.3')
        key.add(btn0)
        text4 = text4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text4, reply_markup=key)

    # Категория Motivation
    elif call.data == 'motiv':
        global text5
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_1.4')
        key.add(btn0)
        text5 = text5
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text5, reply_markup=key)

    # Назад в самое первое меню
    elif call.data in ['back_1','back_2','back_3','back_4']:
        text0 = "Hi 👋\nI'm the bot where you can find Quotes for your heart!\nClick the 📖 Quotes button👇 to continue\nGood luck to find Quotes"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text0, reply_markup=key2)

    # Назад в меню категорий цитат
    elif call.data in ['back_1.1','back_1.2','back_1.3','back_1.4']:
        text1 = 'Choose the category of 📖 Quotes:'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1, reply_markup=key3)


    # Help
    elif call.data == "help":
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_2')
        key.add(btn0)
        text1_0 = '⚫ Cho zdes ne ponatno Blet!\n⚫ Click on 📖 Quotes button in main menu'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1_0, reply_markup=key)


    # About
    elif call.data == "about":
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_3')
        key.add(btn0)
        text1_1 = '⚫ This bot is a child of a student.Who learns programming in TJK-Dushanbe.\n'
        text1_2 = "⚫ It's simple bot where you can find quotes for your heart."
        text1_3 = text1_1 + text1_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1_3, reply_markup=key)


    # Language
    elif call.data == "lang":
        key = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='🇬🇧 English', callback_data='eng')
        btn2 = types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='rus')
        btn0 = types.InlineKeyboardButton(text='↩ Back to the main', callback_data='back_4')
        key.add(btn1)
        key.add(btn2)
        key.add(btn0)
        text_1 = 'Choose the language you want 🏳️:'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text_1, reply_markup=key)

bot.infinity_polling()
