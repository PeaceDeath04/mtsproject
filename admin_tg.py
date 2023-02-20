from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from sqlite import db_start,edit_profile,create_profile,edit_opros,create_opros,update_table
from main import dp,bot 
from markups import but_admin_menu as menu

admin_id = 967282513

class StateGroupHelol(StatesGroup):
    """Машина Состояний StateGroup
       Здесь инициализируются этапы опросов/анкетирования клиента"""

    Question1 = State()
    Question2 = State()

@dp.message_handler(chat_id=admin_id,text='admin')
async def admin_menu(msg: types.Message):
    await bot.send_message(chat_id=admin_id, text='заходит улитка в бар',reply_markup=menu)

@dp.callback_query_handler(chat_id=admin_id,text='helol_txt')
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Напиши приветственный текст')
    await StateGroupHelol.Question1.set()

@dp.message_handler(chat_id=admin_id,state=StateGroupHelol.Question1)
async def helolRename(msg: types.Message,state: FSMContext):
    update_table('HelolText',msg.text)
    await state.finish()

@dp.callback_query_handler(chat_id=admin_id,text='plus_txt')
async def admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Напиши Текст в чем наши плюсы')
    await StateGroupHelol.Question2.set()

@dp.message_handler(chat_id=admin_id,state=StateGroupHelol.Question2)
async def helolRename(msg: types.Message,state: FSMContext):
    update_table('WherePlus',msg.text)
    await state.finish()





