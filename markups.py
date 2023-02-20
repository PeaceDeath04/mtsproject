from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

but_menu = InlineKeyboardButton('Вернуться в главное меню', callback_data='main')

#region Админ панель
but_admin_menu = InlineKeyboardMarkup(row_width=2)
but_adm = InlineKeyboardButton('Изменить Приветствие', callback_data='helol_txt')
but_adm1 = InlineKeyboardButton('Изменить Текст В чем наши плюсы?', callback_data='plus_txt')
but_admin_menu.row(but_adm)
but_admin_menu.row(but_adm1)

reverse_admin_menu = InlineKeyboardMarkup(row_width=1)
reverse_admin_but = InlineKeyboardButton('Вернуться в админ меню',callback_data='admin')
reverse_admin_menu.row(reverse_admin_but)
#endregion



