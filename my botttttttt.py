from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



dp = Dispatcher(bot, storage=MemoryStorage())

# ******Клавиатура Основа********
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
zakaz = types.KeyboardButton("Сделать заказ")
about = types.KeyboardButton("О нас")
needhelp = types.KeyboardButton("Нужна помощь")
kb.add(zakaz, about,needhelp)

# ******Клавиатура помощь********
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
FAQ = types.KeyboardButton("FAQ")
operator = types.KeyboardButton("Связаться с оператором")
otziv = types.KeyboardButton("Оставить отзыв")
kb_help.add(FAQ, operator,otziv)

#Клавиатура FAQ
faq = types.InlineKeyboardMarkup()
faq_1 = InlineKeyboardButton(text="Минимальная стоимость для доставки?", callback_data="faq_1")
faq_2 = InlineKeyboardButton(text="Как свзязаться с вами? ", callback_data="faq_2")
faq_3 = InlineKeyboardButton(text="Какие есть спосбы оплаты товара? ", callback_data="faq_3")
faq.add(faq_1, faq_2, faq_3)






@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_photo(message.chat.id, "https://media.nashaspravka.ru/attachments/db/firms/0/1/1901/thumb_1510862393-9b5320ebd6.png")
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я чат-бот Япономания / роллы суши пицца / доставка Киров.\nНажмите на /help, чтобы узнать подробнее.",reply_markup=kb)


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    mess = '''/start - начало работы с ботом
/information - информация о нашей компании Япономания
/help - помощь
/delivery - информация о зонах доставки
/record - сделать заказ'''
    await bot.send_message(chat_id=message.from_user.id,
                           text=mess, reply_markup=kb)


@dp.message_handler(lambda message: message.text == "Нужна помощь")
async def about_help(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://askanny.com/images/callcentr.png")
    await message.reply(
        'Нужна помощь? Мы всегда рады вам помочь!',reply_markup=kb_help)


@dp.message_handler(lambda message: message.text == "FAQ")
async def about_help(message: types.Message):
    await message.reply('Часто задаваемые вопросы:', reply_markup=faq)

@dp.callback_query_handler(text_contains='faq_')
async def faqqq(call: types.CallbackQuery):
    if call.data and call.data.startswith("faq_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('Минимальная стоимость доставки состовляет от 395р', reply_markup=faq)
        if code == 2:
            await call.message.edit_text('''Общая почта
marketing@yaponomaniya.com
По вопросам рекламы
marketing@yaponomaniya.com
Почта директора
director@yaponomaniya.com''', reply_markup=faq)
        if code == 3:
            await call.message.edit_text('''Вы можете оплатить картой курьеру(на телефоном);\nНаличными;\nКартой на сайте: https://yaponomaniya.com''', reply_markup=faq)
        else:
            await bot.answer_callback_query(call.id)

@dp.message_handler(lambda message: message.text == "Связаться с оператором")
async def about_help(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    await message.reply('Вы можете обратиться к любому из доступных операторов:')
    button1 = types.InlineKeyboardButton("Куликов Иван", url='https://t.me/E_0n9in')
    button2 = types.InlineKeyboardButton('Яшкин Даниил', url='https://t.me/SpEedWaGoNOneLove')
    button3 = types.InlineKeyboardButton('Яровиков Илья', url='https://t.me/slend1954')
    markup.add(button1, button2, button3)
    await message.reply('Вы можете обратиться к любому из доступных операторов:')
    await bot.send_message(message.chat.id,reply_markup=markup)


@dp.message_handler(lambda message: message.text == "О нас")
async def about_information(message: types.Message):
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
async def about_information(message: types.Message):
    info = '''Как давно работает компания? Япономания начала работать в сфере доставки еды одной из первых в Кирове, ещё в 2011 году. Мы приняли уже более 500 000 заказов. Многие клиенты стали постоянными — для нас это очень ценно. Мы рады, что вы с нами'''
    await bot.send_message(chat_id=message.from_user.id,text=info, reply_markup=kb)

@dp.message_handler(lambda message: message.text == "/delivery")
async def about_information(message: types.Message):
    delivery = '''Киров:\nул. Спасская, 17 / Ленина, 82
ул. Московская, 185а\nОктябрьский пр-т, 19\nКоминтерновская пл.1Б (ТЦ Клён, левое крыло)\n
Кирово-Чепецк:
ул. Фестивальная, 5\nул. Володарского, 9\nпр-т России, 34 (ТЦ "Россия", 2 этаж)'''
    await bot.send_message(chat_id=message.from_user.id,text=delivery, reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)