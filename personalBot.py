import telebot
from telebot import types

bot = telebot.TeleBot("5784091321:AAHRnZasSaDVHgaOHtBgduuTdrU2qdc1a7A")

# Вызов start через /start
@bot.message_handler(commands=["start"])
def start_menu(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("IT-Run", callback_data="run")
    key.add(btn1)
    text0 = "Hello 👋"
    bot.send_message(chat_id=msg.chat.id, text=text0, reply_markup=key)

# Вызов IT - Run через /run
@bot.message_handler(commands=["run"])
def run(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Python", callback_data="py"')
    btn2 = types.InlineKeyboardButton(text="Turtle", callback_data="tur")
    btn3 = types.InlineKeyboardButton(text="Pygame", callback_data="game")
    btn4 = types.InlineKeyboardButton(text="Telegrambot", callback_data="telebot")
    btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1")
    key.add(btn1, btn2, btn3, btn4, btn0)
    text1 = "Choose the category of Courses:"
    bot.send_message(chat_id=msg.chat.id, text=text1, reply_markup=key)

# Вызов help через /help
@bot.message_handler(commands=["help"])
def help(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_2")
    key.add(btn0)
    text1_0 = "⚫ What you didn't understand \n ⚫ Click on Courses button in main menu"
    bot.send_message(chat_id=msg.chat.id, text=text1_0, reply_markup=key)

# Вызов about через /about
@bot.message_handler(commands=["about"])
def about(msg: types.Message):
    key = types.InlineKeyboardMarkup()
    btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_3")
    key.add(btn0)
    text1_1 = "⚫ This bot about IT - Run's courses \n"
    text1_2 = "⚫ It's simple bot where you can find courses which you want to learn."
    text1_3 = text1_1 + text1_2
    bot.send_message(chat_id=msg.chat.id, text=text1_3, reply_markup=key)

# Вызов всех других функций
@bot.callback_query_handler(func=lambda call: True)
def all_functions(call: types.CallbackQuery):

    # Keyboards - start
    key = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("IT-Run", callback_data="run")
    key.add(btn1)

    # Return to the main menu
    key2 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("IT -RUN", callback_data="run")
    btn2 = types.InlineKeyboardButton("💡 Help", callback_data="help")
    btn3 = types.InlineKeyboardButton("📜 About Bot", callback_data="about")
    key2.add(btn1, btn2, btn3)
   
    # Return to category of IT - Run
    key3 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Python", callback_data="py")
    btn2 = types.InlineKeyboardButton(text="Turtle", callback_data="tur")
    btn3 = types.InlineKeyboardButton(text="Pygame", callback_data="game")
    btn4 = types.InlineKeyboardButton(text="Telegrambot", callback_data="telebot")
    btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1")
    key3.add(btn1,btn2, btn3, btn4, btn0)

    # Вызов IT - Run  
    if call.data == "run":
        text1 = "Choose the category of Courses:"
        key = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Python", callback_data="py")
        btn2 = types.InlineKeyboardButton(text="Turtle", callback_data="tur")
        btn3 = types.InlineKeyboardButton(text="Pygame", callback_data="game")
        btn4 = types.InlineKeyboardButton(text="Telegrambot", callback_data="telebot")
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1")
        key.add(btn1,btn2, btn3, btn4, btn0)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1, reply_markup=key)

    # Категория Python
    elif call.data == "py":
        global text2
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1.1")
        key.add(btn0)
        text2 = text2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text2, reply_markup=key)

    # Категория Turtle
    elif call.data == "tur":
        global text3
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1.2")
        key.add(btn0)
        text3 = text3
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text3, reply_markup=key)

    # Категория Pygame
    elif call.data == "game":
        global text4
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1.3")
        key.add(btn0)
        text4 = text4
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text4, reply_markup=key)

    # Категория Telegrambot
    elif call.data == "telebot":
        global text5
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main", callback_data="back_1.4")
        key.add(btn0)
        text5 = text5
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text5, reply_markup=key)

    # Назад в самое первое меню
    elif call.data in ["back_1", "back_2", "back_3", "back_4"]:
        text0 = "Hello 👋 \n I'm the bot where you can find courses which you want to learn. \n Click the 📖 Courses button👇 to continue \n Good luck to find Courses"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text0, reply_markup=key2)

    # Назад в меню категорий цитат
    elif call.data in ["back_1.1", "back_1.2", "back_1.3", "back_1.4"]:
        text1 = "Choose the category of 📖 Courses:"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1, reply_markup=key3)


    # Help
    elif call.data == "help":
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main",, callback_data="back_2")
        key.add(btn0)
        text1_0 = "⚫ What you didn't understand \n ⚫ Click on 📖 Courses button in main menu"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1_0, reply_markup=key)


    # About
    elif call.data == "about":
        key = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="↩ Back to the main",, callback_data="back_3")
        key.add(btn0)
        text1_1 = "⚫ This bot about IT - Run's courses \n"
        text1_2 = "⚫ It's simple bot where you can find courses which you want to learn."
        text1_3 = text1_1 + text1_2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text1_3, reply_markup=key)


bot.infinity_polling()
