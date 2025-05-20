"""
Модуль контроллера, отвечающий за основную логику работы приложения.
Содержит главную функцию run(), которая управляет основным потоком выполнения программы.
"""

from config import msg
from model.cl import contacts
from view import show, enter
from controller import actions

def run() -> None:
    """
    Основная функция, управляющая потоком выполнения программы.
    
    Функция отображает меню опций и обрабатывает выбор пользователя:
    - 1: Просмотр всех контактов
    - 2: Создание нового контакта
    - 3: Поиск контактов
    - X: Выход из программы
    
    Returns:
        None
    """
    show.options()
    option = enter.option(msg.select_opt)

    if option == '1':
        show.all_(contacts.book)
        actions.modify_or_delete()

    elif option == '2':
        actions.create_contact()

    elif option == '3':
        show.alert(msg.search_text)
        actions.global_search()

    elif option == msg.X:
        show.alert(msg.bye)
        exit()

    return run()

if __name__ == '__main__':
    run()