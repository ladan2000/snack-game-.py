import telebot
from telebot import types

# توکن ربات خود را در اینجا قرار دهید
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('جمع')
    button2 = types.KeyboardButton('تفریق')
    button3 = types.KeyboardButton('تقسیم')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "لطفاً یکی از عملیات مورد نظر را انتخاب کنید:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    operation = message.text
    if operation == 'جمع':
        bot.send_message(message.chat.id, "عدد اول را وارد کنید:")
        bot.register_next_step_handler(message, process_number1, operation)
    elif operation == 'تفریق':
        bot.send_message(message.chat.id, "عدد اول را وارد کنید:")
        bot.register_next_step_handler(message, process_number1, operation)
    elif operation == 'تقسیم':
        bot.send_message(message.chat.id, "عدد اول را وارد کنید:")
        bot.register_next_step_handler(message, process_number1, operation)
    else:
        bot.send_message(message.chat.id, "لطفاً یکی از گزینه‌های معتبر را انتخاب کنید.")

def process_number1(message, operation):
    if message.text.isdigit():
        number1 = int(message.text)
        bot.send_message(message.chat.id, "عدد دوم را وارد کنید:")
        bot.register_next_step_handler(message, process_number2, operation, number1)
    else:
        bot.send_message(message.chat.id, "لطفاً عدد صحیح وارد کنید.")

def process_number2(message, operation, number1):
    if message.text.isdigit():
        number2 = int(message.text)
        result = 0
        if operation == 'جمع':
            result = number1 + number2
        elif operation == 'تفریق':
            result = number1 - number2
        elif operation == 'تقسیم':
            if number2 != 0:
                result = number1 / number2
            else:
                bot.send_message(message.chat.id, "تقسیم بر صفر امکان‌پذیر نیست.")
                return
        bot.send_message(message.chat.id, f"نتیجه: {result}")
    else:
        bot.send_message(message.chat.id, "لطفاً عدد صحیح وارد کنید.")

bot.polling()
