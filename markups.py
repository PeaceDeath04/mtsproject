from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

but_menu = InlineKeyboardButton('Вернуться в главное меню', callback_data='main')

#region Админ панель
but_admin_menu = InlineKeyboardMarkup(row_width=2)
but_adm0 = InlineKeyboardButton('Изменить Приветствие', callback_data='helol_txt')
but_adm1 = InlineKeyboardButton('Изменить Текст В чем наши плюсы?', callback_data='plus_txt')
but_adm2 = InlineKeyboardButton('Изменить тариф', callback_data='edit_tarif')
but_admin_menu.row(but_adm0)
but_admin_menu.row(but_adm1)
but_admin_menu.row(but_adm2)

reverse_admin_menu = InlineKeyboardMarkup(row_width=1)
reverse_admin_but = InlineKeyboardButton('Вернуться в админ меню',callback_data='admin')
reverse_admin_menu.row(reverse_admin_but)
#endregion



