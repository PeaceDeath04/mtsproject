from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

but_menu = InlineKeyboardButton('Вернуться в главное меню', callback_data='main')

StartMenu = InlineKeyboardMarkup()
StartOprosBut = InlineKeyboardButton("Начать", callback_data="opros")
StartMenu.row(StartOprosBut)


MainMenu = InlineKeyboardMarkup(row_width=3)
MainMenuBut1 = InlineKeyboardButton("Сверить цены",callback_data='sverit')
MainMenuBut2 = InlineKeyboardButton("Заполнить заявку онлайн", callback_data='online')
MainMenuBut3 = InlineKeyboardButton("Позвонить на номер сотрудника",callback_data='phone')
MainMenu.row(MainMenuBut1)
MainMenu.row(MainMenuBut2)
MainMenu.row(MainMenuBut3)

#region Админ панель
#region Главное меню
but_admin_menu = InlineKeyboardMarkup(row_width=2)
but_adm0 = InlineKeyboardButton('Изменить Приветствие', callback_data='helol_txt')
but_adm1 = InlineKeyboardButton('Изменить Текст В чем наши плюсы?', callback_data='plus_txt')
but_adm2 = InlineKeyboardButton('Изменить тариф', callback_data='edit_tarif')
but_admin_menu.row(but_adm0)
but_admin_menu.row(but_adm1)
but_admin_menu.row(but_adm2)
#endregion
#region вернуться в главное меню
reverse_admin_menu = InlineKeyboardMarkup(row_width=1)
reverse_admin_but = InlineKeyboardButton('Вернуться в админ меню',callback_data='admin')
reverse_admin_menu.row(reverse_admin_but)
#endregion
#endregion



