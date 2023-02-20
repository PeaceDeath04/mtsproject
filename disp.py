from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot("6186713037:AAFha_dzFRm0QzyC3waYXI45tmIaMBmYB60",parse_mode = 'html')
dp = Dispatcher(bot,storage=storage)
admin_id = 967282513