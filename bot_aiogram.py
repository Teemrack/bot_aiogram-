from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = aiogram.Bot(token='5809426612:AAFwPNFN8OIp2kFPYM_bv6jWxC7ZmmmbHqM')
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

# ******Клавиатура 1********
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
zakaz = aiogram.types.KeyboardButton("Сделать заказ")
about = aiogram.types.KeyboardButton("О нас")
needhelp = aiogram.types.KeyboardButton("Нужна помощь")
kb.add(zakaz, about,needhelp)


@dp.message_handler(commands=["start"])
async def start_command(message: aiogram.types.Message):
    await bot.send_photo(message.chat.id, "https://media.nashaspravka.ru/attachments/db/firms/0/1/1901/thumb_1510862393-9b5320ebd6.png")
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я чат-бот Япономания / роллы суши пицца / доставка Киров.\nНажмите на /help, чтобы узнать подробнее.",reply_markup=kb)


@dp.message_handler(commands=["help"])
async def help_command(message: aiogram.types.Message):
    mess = '''/start - начало работы с ботом
/information - информация о нашей компании Япономания
/help - помощь
/delivery - информация о зонах доставки
/record - сделать заказ'''
    await bot.send_message(chat_id=message.from_user.id,
                           text=mess, reply_markup=kb)


@dp.message_handler(lambda message: message.text == "О нас")
async def about_pciholog(message: aiogram.types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://sun9-35.userapi.com/impg/8p-RvP4coMaSMxFEAJaRBB2LyM8obhpH_T8z7A/n88I0r6uEto.jpg?size=1080x1080&quality=95&sign=b0e3ff1e63c9e8fb8a6a0c19b8c162dc&type=album")
    await message.reply(
        '''🍣Доставка и Самовывоз: Киров, Кирово-Чепецк
❤ Приём заказов с 10:00 до 23:00 7 дней в неделю!
❤ Получай подарок при первом заказе через 👨‍💻 ЧАТ-БОТ, переходи по ссылке https://vk.me/yaponomaniya и пиши Хочу подарок
❤Единый телефон для приема заказов по Кирову и Кирово-Чепецку: +7(8332) 735-166.
🔥Наши адреса:
✔Киров, ул. Спасская, 17/Ленина, 82
✔Киров, ул. Московская, 185а
✔Киров, Октябрьский пр-т, 19
✔Киров, ТЦ Клён, Коминтерновская пл., д.1
✔Кирово-Чепецк, ул. Фестивальная, 5
✔Кирово-Чепецк, ул. Володарского, 9
✔Кирово-Чепецк, ТЦ Россия, 2 этаж, проспект России, 34
🍣Бесплатная доставка от 395 рублей (Киров, Кирово-Чепецк)
✔Способы оплаты: https://vk.com/topic-30551885_39596406''')

@dp.message_handler(lambda message: message.text == "/information")
async def about_information(message: aiogram.types.Message):
    info = '''Как давно работает компания. Япономания начала работать в сфере доставки еды одной из первых в Кирове, ещё в 2011 году. Мы приняли уже более 500 000 заказов. Многие клиенты стали постоянными — для нас это очень ценно.'''
    await bot.send_message(chat_id=message.from_user.id,text=info, reply_markup=kb)

@dp.message_handler(lambda message: message.text == "/delivery")
async def about_information(message: aiogram.types.Message):
    delivery = '''Киров:\nул. Спасская, 17 / Ленина, 82
ул. Московская, 185а\nОктябрьский пр-т, 19\nКоминтерновская пл.1Б (ТЦ Клён, левое крыло)\n
Кирово-Чепецк:
ул. Фестивальная, 5\nул. Володарского, 9\nпр-т России, 34 (ТЦ "Россия", 2 этаж)'''
    await bot.send_message(chat_id=message.from_user.id,text=delivery, reply_markup=kb)











if __name__ == "__main__":
    aiogram.executor.start_polling(dispatcher=dp)