from config import msg
from controller import validate


def option(prompt: str):

    """Запрос пункта главного меню"""

    choice = input(prompt)
    if validate.option(choice):
        return choice
    else:
        print(msg.input_err)
        return option(prompt)


def confirm(prompt: str):

    """Подтверждение действия [y]/[n]"""

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


def mod_or_del(prompt: str, ok=True):

    """Запрос на изменение [m] или удаление [d] контакта или отмена [x]"""

    action = input(prompt).lower()
    if validate.mode(action):
        if action == msg.X:
            return False, None
        return ok, action
    else:
        print(msg.input_err)
        return mod_or_del(prompt)


def cid(prompt: str, ok=True):

    """Запрос ID контакта или отмена [x]"""

    contact_id = input(prompt).upper()
    if validate.cid(contact_id):
        if contact_id == msg.X.upper():
            return False, None
        return ok, contact_id
    else:
        print(msg.id_err)
        return cid(prompt)


def mod_value(detected_id, ok=True):

    """Запрашиваем какой параметр найденного контакта с ID {detected_id} поменять"""

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
        return ok, field , new_value
    else:
        print(msg.field_err)
        return mod_value(detected_id)


def phone(prompt):

    """Запрашиваем номер телефона и проверяем ввод"""

    phone_value = input(prompt)
    if validate.phone(phone_value):
        if phone_value == msg.X:
            return False
        return phone_value
    else:
        print(msg.phone_format_err)
        return phone(prompt)


def new_contact(fields_input: dict):

    """Запрашиваем данные для контакта"""

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


def look_up():

    """Запрашиваем строку поиска"""

    search_str = input(msg.ask.search)
    if validate.search(search_str):
        if search_str == msg.X:
            return False
        return search_str.lower()
    print(msg.input_err)
    return look_up()


if __name__ == '__main__':
    pass
