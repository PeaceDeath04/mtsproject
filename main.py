import asyncio
import aiogram.dispatcher
from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import admin_tg
from disp import bot,dp,storage

from sqlite import db_start,edit_profile,create_profile,edit_opros,create_opros,show_on_bd
from texts import questions,answers,tarif_on_sale




#region Инициализация бота и дспетчера асинхронности

#endregion

#region Методы для тг

async def on_startup(_):
    """Метод on_startup\n
       При Запуске программы main.py происходит проверка на наличие или создание дата базы
       также сюда можно подставить любой метод, который вы хотите вызвать в начале запуска программы"""

    await db_start()

class StateGroupOpros(StatesGroup):
    """Машина Состояний StateGroup
       Здесь иницпплвЫВОВПЫОПВиализируются этапы опросов/анкетирования клиента"""
    Question1 = State()
    Question2 = State()
    Question3 = State()
    Question4 = State()
    Question5 = State()
    End_opros = State()
    Sverka = State()
    Fio = State()
    contact_num = State()
    adress = State()

async def SetInlineBut(answ):
    """Set In Line But\n
       Метод принимающий определенный индекс массива
       используемый для создания InLine клавиатуры
       '''

        Сначало мы подсчитываем количество элементов массива для подстановки в row_width InLine Клавы.\n

        \nПотом обходим каждый элемент массива создавая его в кнопку , а его Callback data будет называться but_ЭЛЕМЕНТ МАССИВА
        \nЭлемент массива в нашем случае это Определнный ответ на вопрос"""
    kb = InlineKeyboardMarkup(row_width=len(answ))
    i = 0
    while i <len(answ):
        kb.add(InlineKeyboardButton(f'{answ[i]}',callback_data = f'but_{answ[i]}'))
        i+=1
    return kb

async def ClearAnsw(data):
    """Clear Answear
    Метод получаемый call.data форматирующий его в ответ
    для последующего добавления в бд

    :param call.data:
    :return готовый ответ в дата базу:
    """
    call_data = data
    but_press = call_data.split("_")[1]
    return but_press

#endregion

#region Анкетирование


@dp.message_handler(commands=['start'])
async def but_pressed(message: types.Message) -> None:
    await create_profile(message.from_user.id)
    await create_opros(message.from_user.id)
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Начать", callback_data="opros")
    )
    await message.answer(show_on_bd('HelolText'),reply_markup= markup)

@dp.callback_query_handler(text=["opros"])
async def btn_pressed(call: types.CallbackQuery):
    markup = await SetInlineBut(answers[0])
    await call.message.edit_text(f"{questions[0]}",reply_markup=markup)
    await call.answer()
    await StateGroupOpros.Question1.set()

@dp.callback_query_handler(Text(startswith='but_'),state=StateGroupOpros.Question1)
async def que1(call: types.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        data['question1'] = await ClearAnsw(call.data)
    markup = await SetInlineBut(answers[1])
    await call.message.edit_text(f"{questions[1]}",reply_markup=markup)
    await call.answer()
    await StateGroupOpros.next()

@dp.callback_query_handler(Text(startswith='but_'),state=StateGroupOpros.Question2)
async def que2(call: types.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        data['question2'] = await ClearAnsw(call.data)
    markup = await SetInlineBut(answers[2])
    await call.message.edit_text(f"{questions[2]}",reply_markup=markup)
    await call.answer()
    await StateGroupOpros.next()

@dp.callback_query_handler(Text(startswith='but_'),state=StateGroupOpros.Question3)
async def que3(call: types.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        data['question3'] = await ClearAnsw(call.data)
    markup = await SetInlineBut(answers[3])
    await call.message.edit_text(f"{questions[3]}",reply_markup=markup)
    await call.answer()
    await StateGroupOpros.next()

@dp.callback_query_handler(Text(startswith='but_'),state=StateGroupOpros.Question4)
async def que4(call: types.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        data['question4'] = await ClearAnsw(call.data)
    markup = await SetInlineBut(answers[3])
    await call.message.edit_text(f"{questions[4]}",reply_markup=markup)
    await call.answer()
    await StateGroupOpros.End_opros.set()

@dp.callback_query_handler(Text(startswith='but_'),state=StateGroupOpros.End_opros)
async def que5(call: types.CallbackQuery,state: FSMContext):
    async with state.proxy() as data:
        data['question5'] = await ClearAnsw(call.data)

    await call.message.edit_text(f'Большое спасибо за прохождение опроса\n'
                                 f'Мы готовы предложить вам \n'+
                                 '\n'.join(map(', '.join, tarif_on_sale)))
    markup = InlineKeyboardMarkup(row_width=3)
    but1 = InlineKeyboardButton("Сверить цены",callback_data='sverit')
    but2 = InlineKeyboardButton("Заполнить заявку онлайн", callback_data='online')
    but3 = InlineKeyboardButton("Позвонить на номер сотрудника",callback_data='phone')
    markup.row(but1)
    markup.row(but2)
    markup.row(but3)

    await bot.send_message(call.message.chat.id,text='Мы лучшие в своем деле и нам нечего скрывать ! Вы можете самостоятельно сверить цены услуг других операторов Или же оставить заявку По одному из выбранных вариантов : Заполнить заявку онлайн или связаться с сотрудником',reply_markup=markup)
    await edit_opros(call.message.chat.id,data)

    await call.answer()
    await state.finish()
@dp.callback_query_handler(text='online')
async def onlineZayav(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text('Для начала напишите Фио')
    await StateGroupOpros.Fio.set()

@dp.message_handler(state=StateGroupOpros.Fio)
async def fio(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['Фамилия'],data['Имя'],data['Отчество'] = (msg.text.split() + [''] * 3)[:3]
    await bot.send_message(msg.from_user.id,'Теперь напишите контактный номер телефона')
    await StateGroupOpros.contact_num.set()

@dp.message_handler(state=StateGroupOpros.contact_num)
async def cont_num(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['Номер Телефона'] = msg.text
    await bot.send_message(msg.from_user.id,'Теперь напишите Адрес, Пример: Пушкина 35 14 (улица дом квартира)')
    await StateGroupOpros.adress.set()

@dp.message_handler(state=StateGroupOpros.adress)
async def adress(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['Улица'],data['Дом'],data['Квартира'] = (msg.text.split() + [''] * 3)[:3]

    markup = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton('Главное меню',callback_data='main')
    markup.add(but1)
    await bot.send_message(msg.from_user.id,'Отлично Ваша заявка отправлена!Ожидайте звонка!',reply_markup=markup)
    await edit_profile(msg.from_user.id,data)
    await state.finish()

@dp.callback_query_handler(text='main')
async def main_menu(call: types.CallbackQuery):
    menu = InlineKeyboardMarkup(row_width=3)
    but1 = InlineKeyboardButton("Сверить цены", callback_data='sverit')
    but2 = InlineKeyboardButton("Заполнить заявку онлайн", callback_data='online')
    but3 = InlineKeyboardButton("Позвонить на номер сотрудника",callback_data='phone')
    menu.row(but1)
    menu.row(but2)
    menu.row(but3)

    await call.message.edit_text('Вы зашли главное меню',reply_markup=menu)
@dp.callback_query_handler(text='sverit')
async def sverka(call: types.CallbackQuery):
    sverkamenu = InlineKeyboardMarkup(row_width=6)
    but1 = InlineKeyboardButton("Мтс", url="https://perm.mts.ru/personal/dom/home-allmts/perm-city")
    but2 = InlineKeyboardButton("Билайн", url='https://beeline.lnternet.online/')
    but3 = InlineKeyboardButton("Ростелеком", url="https://perm.rt.ru/homeinternet/internet_tv_mobile")
    but4 = InlineKeyboardButton("Dom ru", url="https://perm.dom.ru/internet")
    but5 = InlineKeyboardButton('В чем наши плюсы над остальными?',callback_data='plusi')
    but6 = InlineKeyboardButton('Вернуться в главное меню', callback_data='main')
    sverkamenu.row(but1)
    sverkamenu.row(but2,but3,but4)
    sverkamenu.row(but5)
    sverkamenu.row(but6)
    await call.message.edit_text('Нажимая кнопки вы можете перейти по ссылке и ознакомится с ценами их предлогаемыми условиями',reply_markup=sverkamenu)
@dp.callback_query_handler(text='plusi')
async def plusi(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    main_but = InlineKeyboardButton('Вернуться в главное меню',callback_data='main')
    markup.row(main_but)
    await call.message.edit_text(show_on_bd('WherePlus'),reply_markup=markup)
@dp.callback_query_handler(text ='phone')
async def phone(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    main_but = InlineKeyboardButton('Вернуться в главное меню', callback_data='main')
    markup.row(main_but)
    await call.message.edit_text('Позвоните по этому номеру 8923818160, Рабочее время с 10 до 22:00',reply_markup=markup)
#endregion

#region запуск бота
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
#endregion