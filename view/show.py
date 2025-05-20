"""
Модуль отображения данных.
Содержит функции для вывода информации в консоль в различных форматах.
"""

from config import msg
from prettytable import PrettyTable


def options() -> None:
    """
    Отображает меню опций программы.
    """
    print(msg.opt)
    for i, option in enumerate(msg.options, start=1):
        print(f"\t[{i}] {option}")
    print(msg.esc)


def all_(cont_dict: dict) -> None:
    """
    Отображает все контакты в виде таблицы.
    
    Args:
        cont_dict (dict): Словарь контактов
    """
    ctable = PrettyTable()
    ctable.field_names = ['#',
                          'ID',
                          'Name/Nickname',
                          'Surname',
                          'Phone',
                          'Comment',
                          'Tags',
                          'Created',
                          'Modified',
                          ]

    for i, (cid, info) in enumerate(cont_dict.items(), start=1):
        ctable.add_rows(
            [
                [
                 i, cid,
                 info.get(msg.NAME, 'N/A'),
                 info.get(msg.SURN, 'N/A'),
                 info.get(msg.PHONE, 'N/A'),
                 info.get(msg.NOTE, 'N/A'),
                 info.get(msg.TAGS, 'N/A'),
                 info.get(msg.CREATED, 'N/A'),
                 info.get(msg.MODIFIED, 'N/A')
                ]
            ]
        )

    print('', ctable, sep='\n')


def one_(cont_dict: dict, detect_id: str) -> None:
    """
    Отображает информацию об одном контакте.
    
    Args:
        cont_dict (dict): Словарь контактов
        detect_id (str): ID контакта для отображения
    """
    print(f'\nID: {detect_id}, {cont_dict[detect_id].get(msg.CREATED, "N/A")}')
    print(f'Name/Nickname : {cont_dict[detect_id].get(msg.NAME, "N/A")}')
    print(f'Surname       : {cont_dict[detect_id].get(msg.SURN, "N/A")}')
    print(f'Phone number  : {cont_dict[detect_id].get(msg.PHONE, "N/A")}')
    print(f'Comment   : {cont_dict[detect_id].get(msg.NOTE)}')
    print(f'Tags : {cont_dict[detect_id].get(msg.TAGS, "N/A")}')
    print('---')


def alert(txt: str) -> None:
    """
    Отображает сообщение в рамке.
    
    Args:
        txt (str): Текст сообщения
    """
    separator = f'\t{'-' * len(txt)}'
    print(f'\n{separator}')
    print(f'\t{txt}')
    print(f'{separator}\n')


if __name__ == "__main__":
    options()
    alert('very long test message')