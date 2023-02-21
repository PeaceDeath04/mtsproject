from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from sqlite import db_start,edit_profile,create_profile,edit_opros,create_opros,update_table,update_tarif
from main import dp,bot 
from markups import but_admin_menu,reverse_admin_menu

admin_id = 967282513

#region Машина состояний
class StateGroupHelol(StatesGroup):
    """Машина Состояний StateGroup
       Здесь изменяется текст сохранением его в бд"""

    Question1 = State()
    Question2 = State()

class StateGroupTarifGet(StatesGroup):
    """Машина Состояний StateGroup
      Здесь заполняется тариф в бд """

    StateMain = State()
    StateCaption = State()

class StateGroupQuestion(StatesGroup):
    """Машина Состояний StateGroup
      Здесь заполняется тариф в бд """

    Que1 = State()
    Que2 = State()
    Que3 = State()
    Que4 = State()
    Que5 = State()
#endregion

#region Админ панель
@dp.message_handler(chat_id=admin_id,text='admin')
async def admin_menu(msg: types.Message):
    await bot.send_message(chat_id=admin_id, text='Меню админа',reply_markup=but_admin_menu)

@dp.callback_query_handler(chat_id=admin_id,text='admin')
async def admin_menu(msg: types.Message):
    await bot.send_message(chat_id=admin_id, text='Меню админа',reply_markup=but_admin_menu)

#endregion

#region изменение Сообщения
@dp.callback_query_handler(chat_id=admin_id,text='helol_txt')
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Напиши приветственный текст')
    await StateGroupHelol.Question1.set()

@dp.message_handler(chat_id=admin_id,state=StateGroupHelol.Question1)
async def helolRename(msg: types.Message,state: FSMContext):
    update_table('HelolText',msg.text)
    await state.finish()
    await bot.send_message(chat_id=admin_id, text='Текст успешно изменён', reply_markup=reverse_admin_menu)

@dp.callback_query_handler(chat_id=admin_id,text='plus_txt')
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Напиши Текст в чем наши плюсы')
    await StateGroupHelol.Question2.set()

@dp.message_handler(chat_id=admin_id,state=StateGroupHelol.Question2)
async def helolRename(msg: types.Message,state: FSMContext):
    update_table('WherePlus',msg.text)
    await state.finish()
    await bot.send_message(chat_id=admin_id, text='Текст успешно изменён', reply_markup=reverse_admin_menu)
#endregion

#region изменение тарифа
@dp.callback_query_handler(chat_id=admin_id,text='edit_tarif')
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Дайте Название тарифу')
    await StateGroupTarifGet.StateMain.set()
@dp.message_handler(chat_id=admin_id,state=StateGroupTarifGet.StateMain)
async def editMainText(msg: types.Message,state: FSMContext):
    update_tarif('MainName',msg.text)
    await StateGroupTarifGet.StateCaption.set()
    await bot.send_message(chat_id=admin_id, text='Теперь напишите описание тарифа')

@dp.message_handler(chat_id=admin_id,state=StateGroupTarifGet.StateCaption)
async def editMainText(msg: types.Message,state: FSMContext):
    update_tarif('caption',msg.text)
    await state.finish()
    await bot.send_message(chat_id=admin_id, text='Тариф успешно изменён', reply_markup=reverse_admin_menu)


#endregion





