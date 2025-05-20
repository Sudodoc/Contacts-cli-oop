"""
Модуль валидации, содержащий функции для проверки корректности вводимых данных.
Включает проверки для опций меню, подтверждений, ID контактов и других полей.
"""

from config import msg
from model.cl import contacts


def option(opt: str, cancel_value: str = msg.X) -> bool:
    """
    Проверяет корректность выбранной опции меню.
    
    Args:
        opt (str): Введенная опция
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        bool: True если опция корректна, False в противном случае
    """
    if opt == cancel_value or (opt.isdigit() and int(opt) in range(1, len(msg.options) + 1)):
        return True
    return False


def confirm(opt: str, ok_value: str = msg.Y, no_value: str = msg.N) -> bool:
    """
    Универсальная функция проверки корректности подтверждения действия(да/нет).
    
    Args:
        opt (str): Введенное значение
        ok_value (str, optional): Значение для подтверждения. По умолчанию msg.Y
        no_value (str, optional): Значение для отказа. По умолчанию msg.N
        
    Returns:
        bool: True если значение корректно, False в противном случае
    """
    if opt == ok_value or opt == no_value:
        return True
    return False


def mode(opt: str, modify_value: str = msg.M, delete_value: str = msg.D, cancel_value: str = msg.X) -> bool:
    """
    Проверяет корректность выбранного режима (модификация/удаление/отмена).
    
    Args:
        opt (str): Введенное значение
        modify_value (str, optional): Значение для модификации. По умолчанию msg.M
        delete_value (str, optional): Значение для удаления. По умолчанию msg.D
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        bool: True если значение корректно, False в противном случае
    """
    if opt == modify_value or opt == delete_value or opt == cancel_value:
        return True
    return False


def cid(opt: str, cancel_value: str = msg.X) -> bool:
    """
    Проверяет существование ID контакта в справочнике *.json.
    
    Args:
        opt (str): Введенный ID
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        bool: True если ID существует или введена отмена, False в противном случае
    """
    if opt in contacts.book or opt == cancel_value.upper():
        return True 
    return False


def field(opt: str, detected_id: str, cancel_value: str = msg.X) -> bool:
    """
    Проверяет существование параметра (поля) в контакте.
    
    Args:
        opt (str): Введенное значение поля
        detected_id (str): ID контакта
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        bool: True если поле существует или введена отмена, False в противном случае
    """
    if opt in str(contacts.book[detected_id]).lower() or opt == cancel_value:
        return True
    return False


def entry(opt: str | list, cancel_value: str = msg.X) -> str | bool:
    """
    Универсальная проверка корректности введенного значения, где задана одна клавиша отмены.
    
    Args:
        opt (str | list): Введенное значение
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        str | bool: 'N/A' для пустого значения, False для отмены, исходное значение в остальных случаях
    """
    if isinstance(opt, list) and opt[0] == cancel_value:
        return False
    elif opt == '':
        return 'N/A'

    return opt


def phone(opt: str, cancel_value: str = msg.X) -> bool:
    """
    Проверяет корректность формата введенного номера телефона.
    
    Args:
        opt (str): Введенный номер телефона
        cancel_value (str, optional): Значение для отмены. По умолчанию msg.X
        
    Returns:
        bool: True если номер корректный или введена отмена, False в противном случае
    """
    if opt == cancel_value:
        return True

    for char in opt:
        if not (char.isdigit() or char in msg.phone_chars):
            return False

    return True


def search(opt: str) -> bool:
    """
    Проверяет корректность поискового запроса / строки поиска. Исключает пустые строки и поиск по пробелам.
    
    Args:
        opt (str): Поисковый запрос
        
    Returns:
        bool: False для пустого запроса, True в остальных случаях
    """
    if opt == '' or opt == ' ':
        return False
    return True


if __name__ == '__main__':
    pass