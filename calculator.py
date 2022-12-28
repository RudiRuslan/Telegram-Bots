import telebot, datetime, time, math, re 
from telebot import types 

BOT_TOKEN = '5973282393:AAHwgLIrr0VdUyWXNOz27vUrZz1AeGn8rMg' # Токен Телеграм-бота 
BOT_NAME = 'calc_bot' # Имя для бота.
bot = telebot.TeleBot(BOT_TOKEN) 

TIMEOUT_CONNECTION = 5 # Таймаут переподключения 


# Сообщение при старте
START_MESSAGE = """Отправь мне выражение, а я тебе скажу результат)"""
# Сообщение поддержки
HELP_MESSAGE = """Мной пользоваться очень просто. Вы мне отправляете выражение, а я вам возвращаю его результат.

***Операторы***:
    + - сложение;
    - - вычитание;
    \* - умножение;
    / - деление;
    \*\* - возведение в степнь.
    
***Функции***:
    cos(x) - косинус x;
    sin(x) - синус x;
    tg(x) - тангенс x;
    fact(x) - факториал x;
    sqrt(x) - квадратный корень х;
    sqr(x) - х в квадрате.

***Логарифмы***:
    log2(x) - логарифм х по основанию 2;
    lg(х) - десятичный логарифм х;
    ln(x) - натуральный логарифм x;
    log(b, х) - логарифм х по основанию b;

***Системы счисления***:
    0bx - перевести двоичное число х в десятичное;
    0ox - перевести восьмиричное число х в десятичное;
    0xx - перевести шестнадцатиричное число х в десятичное;"""

пи = п = p = pi = 3.141592653589793238462643 # число Пи asd 

# Ниже все понятно...
def fact(float_):
    return math.factorial(float_)

def cos(float_):
    return math.cos(float_)

def sin(float_):
    return math.sin(float_)

def tg(float_):
    return math.tan(float_)
    
def tan(float_):
    return math.tan(float_)


def ln(float_):
    return math.log(float_)

def log(base, float_):
    return math.log(float_, base)

def lg(float_):
    return math.log10(float_)

def log2(float_):
    return math.log2(float_)

def exp(float_):
    return math.exp(float_)

# Обработчик сообщений-команд
@bot.message_handler(commands=['start', 'help'])
def send_start(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    if message.text.lower() == '/start':
        msg = bot.send_message(message.chat.id, START_MESSAGE, parse_mode='markdown')

    elif message.text.lower() == '/help':
        msg = bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode='markdown')
        
    if (msg):
        print('Бот: %s'%msg.text)

# Обработчик всех сообщений
@bot.message_handler(func = lambda message: True)
def answer_to_user(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    user_message = message.text.lower()

    if BOT_NAME:
        regex = re.compile(BOT_NAME.lower())
        print(regex.search(user_message))
        if regex.search(user_message) == None:
            return

        regex = re.compile('%s[^a-z]'%(BOT_NAME.lower()))
        user_message = regex.sub("", user_message)

    user_message = user_message.lstrip()
    user_message = user_message.rstrip()
    
    print(user_message)

    if user_message == 'привет':
        msg = bot.send_message(message.chat.id, '*Привет, %s*'%(message.chat.first_name), parse_mode='markdown')

    elif user_message == 'помощь':
        msg = bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode='markdown')

    else:
        try:
            answer = str(eval(user_message.replace(' ', '')))
            msg = bot.send_message(message.chat.id, user_message.replace(' ', '') + ' = ' + answer)
                
        except SyntaxError:
            msg = bot.send_message(message.chat.id, 'Похоже, что вы написали что-то не так. \nИсравьте ошибку и повторите снова')
        except NameError:
            msg = bot.send_message(message.chat.id, 'Переменную которую вы спрашиваете я не знаю. \nИсравьте ошибку и повторите снова')
        except TypeError:
            msg = bot.send_message(message.chat.id, 'Мне кажется, что в выражении присутствует ошибка типов. \nИсравьте ошибку и повторите снова')
        except ZeroDivisionError:
            msg = bot.send_message(message.chat.id, 'В выражении вы делите на ноль. \nИсравьте ошибку и повторите снова')

    if (msg):
        print('Бот: %s'%msg.text)



# Вход в программу
if (__name__ == '__main__'):
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print ('Ошибка подключения. Попытка подключения через %s сек.'%TIMEOUT_CONNECTION)
            time.sleep(TIMEOUT_CONNECTION)