"""
Модуль ввода данных.
Содержит функции для получения и проверки корректности введенных пользовательских данных.
"""

from config import msg
from controller import validate


def option(prompt: str) -> str:
    """
    Запрашивает и проверяет корректность выбора пункта главного меню.
    
    Args:
        prompt (str): Текст запроса
        
    Returns:
        str: Выбранная опция
    """
    choice = input(prompt)
    if validate.option(choice):
        return choice
    else:
        print(msg.input_err)
        return option(prompt)


def confirm(prompt: str) -> bool | None:
    """
    Запрашивает и проверяет подтверждение действия (да/нет).
    
    Args:
        prompt (str): Текст запроса
        
    Returns:
        bool | None: True для подтверждения, False для отказа, None при ошибке
    """
    yes_or_no = input(prompt).lower()
    if validate.confirm(yes_or_no):
        if yes_or_no == msg.Y:
            return True
        elif yes_or_no == msg.N:
            return False
        return None
    else:
        print(msg.input_err)
        return confirm(prompt)


def mod_or_del(prompt: str, ok: bool = True) -> tuple[bool, str | None]:
    """
    Запрашивает и валидирует выбор между редактированием и удалением контакта.
    
    Args:
        prompt (str): Текст запроса
        ok (bool, optional): Флаг (True по умолчанию),
        если пользователь не инициировал отмену нажатием на клавишу отмены msg.X.
        
    Returns:
        tuple[bool, str | None]: Кортеж (флаг отмены, выбранное действие)
    """
    action = input(prompt).lower()
    if validate.mode(action):
        if action == msg.X:
            return False, None
        return ok, action
    else:
        print(msg.input_err)
        return mod_or_del(prompt)


def cid(prompt: str, ok: bool = True) -> tuple[bool, str | None]:
    """
    Запрашивает и валидирует введенный пользователем ID контакта.
    
    Args:
        prompt (str): Текст запроса
        ok (bool, optional): Флаг (True по умолчанию), если пользователь не инициировал отмену нажатием на клавишу отмены msg.X.
        
    Returns:
        tuple[bool, str | None]: Кортеж (флаг успешности, ID контакта)
    """
    contact_id = input(prompt).upper()
    if validate.cid(contact_id):
        if contact_id == msg.X.upper():
            return False, None
        return ok, contact_id
    else:
        print(msg.id_err)
        return cid(prompt)


def mod_value(detected_id: str, ok: bool = True) -> tuple[bool, str | None, str | list | None]:
    """
    Запрашивает и валидирует поле для модификации контакта.
    
    Args:
        detected_id (str): ID контакта
        ok (bool, optional): Флаг (True по умолчанию), если пользователь не инициировал отмену нажатием на клавишу отмены msg.X.
        
    Returns:
        tuple[bool, str | None, str | None]: Кортеж (флаг успешности, поле, новое значение)
    """
    field = input(msg.ask.field).lower()
    if validate.field(field, detected_id):
        if field == msg.X:
            return False, None, None
        elif field == msg.TAGS:
            new_value = list(set((input(msg.ask.tags)).lower().split(' ')))
        else:
            new_value = input(msg.ask.value)
            if new_value == msg.X:
                return False, None, None
        return ok, field, new_value
    else:
        print(msg.field_err)
        return mod_value(detected_id)


def phone(prompt: str) -> str | bool:
    """
    Запрашивает и валидирует номер телефона.
    
    Args:
        prompt (str): Текст запроса
        
    Returns:
        str | bool: Номер телефона или False при отмене
    """
    phone_value = input(prompt)
    if validate.phone(phone_value):
        if phone_value == msg.X:
            return False
        return phone_value
    else:
        print(msg.phone_format_err)
        return phone(prompt)


def new_contact(fields_input: dict) -> tuple[dict, bool]:
    """
    Последовательно запрашивает данные для нового контакта.
    
    Args:
        fields_input (dict): Словарь с текстами запросов.
        
    Returns:
        tuple[dict, bool]: Кортеж (словарь значений, флаг отмены)
    """
    values = {}
    for field, prompt in fields_input.items():
        if field == msg.TAGS:
            tag_value = validate.entry(list(set((input(prompt)).lower().split(' '))))
            if tag_value:
                values[field] = tag_value
            else:
                return {}, True

        elif field == msg.PHONE:
            phone_value = phone(prompt)
            if phone_value:
                values[field] = phone_value
            else:
                return {}, True

        else:
            field_value = validate.entry(input(prompt))
            if field_value:
                values[field] = field_value
            else:
                return {}, True

    return values, False


def look_up() -> str | bool:
    """
    Запрашивает и валидирует строку поиска.
    
    Returns:
        str | bool: Строка поиска или False при отмене
    """
    search_str = input(msg.ask.search)
    if validate.search(search_str):
        if search_str == msg.X:
            return False
        return search_str.lower()
    print(msg.input_err)
    return look_up()


if __name__ == '__main__':
    pass
