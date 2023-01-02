from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot_films = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton(text='Ссылка на бота', url='https://t.me/jokerouk_bot')
)

cities = ['Гомель', 'Минск', 'Брест', 'Витебск', 'Могилёв', 'Гродно']

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton(cities[0]),
    KeyboardButton(cities[1]),
    KeyboardButton(cities[2])
).row(
    KeyboardButton(cities[3]),
    KeyboardButton(cities[4]),
    KeyboardButton(cities[5])
)

house_or_street = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Что можно поделать дома ?🏠')
).row(
    KeyboardButton('Как можно провести время на улице ?🚶‍♂🚶‍♀')
).row(
    KeyboardButton('Узнать погоду в городе🌤'),
    KeyboardButton('Сыграть в игру🔮')
)

minsk = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Как можно провести время на улице ?🚶‍♂🚶‍♀')
)

help_assistant_house = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Что за акция на пиццу?🍕'),
    KeyboardButton('Какой фильм можно посмотреть?🎬')
).row(
    KeyboardButton('Какую книгу можно почитать?📚')
).row(
    KeyboardButton('Какой десерт можно легко приготовить?🧁')
).row(
    KeyboardButton('Узнать погоду в городе🌤')
).row(
    KeyboardButton('Как можно провести время на улице ?🚶‍♂🚶‍♀')
)

help_assistant_street = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('На какой фильм в кинотеатр можно сходить ?🎬')
).row(
    KeyboardButton('Куда можно сходить поесть ?🍽')
).row(
    KeyboardButton('Где и какой кофе можно выпить?☕️')
).row(
    KeyboardButton('Узнать погоду в городе🌤'),
    KeyboardButton('Что можно поделать дома ?🏠')
)


me_location = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton(text="Отправить своё местоположение🌏", request_location=True),
    KeyboardButton('Выйти в главное меню📋')
)


menu = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Выйти в главное меню📋')
)

