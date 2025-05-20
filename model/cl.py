"""
Модуль, содержащий классы для работы с контактами.
Включает классы ContactList для управления списком контактов и SingleContact для работы с отдельным контактом.
"""

from typing import Dict
from config import msg
from pathlib import Path
from model import repo, utils
from itertools import zip_longest


class ContactList:
    """
    Класс для управления списком контактов.
    """

    def __init__(self,
                 cont_dict: Dict[str, dict] = repo.cont_file.open(),
                 cont_path: Path = repo.cont_path
                 ):
        """
        Инициализирует список контактов.
        
        Args:
            cont_dict (Dict[str, dict], optional): Словарь контактов.
            По умолчанию загружается из файла contacts.json
            cont_path (Path, optional): Путь к файлу контактов. По умолчанию берется из repo
        """
        self.book = cont_dict
        self.path = cont_path


    def remove(self, detected_id: str) -> None:
        """
        Удаляет контакт по ID.
        
        Args:
            detected_id (str): ID контакта для удаления
        """
        del self.book[detected_id]
        repo.cont_file.save(self.book)

        
    def change(self, detected_id: str, modi_key: str, new_value: str, time_key: str) -> None:
        """
        Изменяет значение поля контакта с заданным ID.
        
        Args:
            detected_id (str): ID контакта
            modi_key (str): Ключ поля для изменения
            new_value (str): Новое значение
            time_key (str): Ключ поля времени изменения данных
        """
        self.book[detected_id][modi_key] = new_value
        self.book[detected_id][time_key] = utils.get_formated_datetime()
        repo.cont_file.save(self.book)


    def search(self, search_str: str, no_result: str = msg.no_result) -> Dict[str, dict] | bool:
        """
        Выполняет поиск контактов по строке.
        
        Args:
            search_str (str): Строка для поиска
            no_result (str, optional): Сообщение при отсутствии результатов. По умолчанию msg.no_result
            
        Returns:
            Dict[str, dict] | bool: Словарь найденных контактов или False, если ничего не найдено
        """
        search_result = {}
        for c_id, contact in self.book.items():
            for item in contact.values():
                if search_str in (str(item)).lower():
                    search_result[c_id] = self.book[c_id]
        if not search_result:
            print(no_result)
            return False
        else:
            return search_result


    def sync(self) -> None:
        """
        Синхронизирует список контактов с файлом *.json
        """
        self.book = repo.cont_file.open()
        print('sync book')


class SingleContact(ContactList):
    """
    Класс для работы с отдельным контактом.
    Наследуется от ContactList.
    """
    def __init__(self, c_count: int, c_name: str, c_surn: str, c_phone: str, c_note: str, c_tags: list, modified: str = None,
                 cont_dict: Dict[str, dict] = repo.cont_file.open(),
                 cont_path: Path = repo.cont_path
                 ):
        """
        Инициализирует контакт.
        
        Args:
            c_count (int): Порядковый номер контакта при его создании. Не является порядковым номером в списке.
            c_name (str): Имя
            c_surn (str): Фамилия
            c_phone (str): Телефон
            c_note (str): Комментарий
            c_tags (list): Теги
            modified (str, optional): Время модификации. По умолчанию None
            cont_dict (Dict[str, dict], optional): Словарь контактов. По умолчанию загружается из файла *.json
            cont_path (Path, optional): Путь к файлу контактов. По умолчанию берется из repo
        """
        super().__init__(cont_dict, cont_path)
        self.cid = utils.gen_id(c_name, c_surn, c_phone, c_count)
        self.name = c_name.capitalize()
        self.surn = c_surn.capitalize()
        self.phone = utils.get_digits(c_phone)
        self.note = c_note
        self.tags = c_tags
        self.count = c_count
        self.created = utils.get_formated_datetime()
        self.modified = modified


    def get(self, ckeys: list = msg.cont_keys) -> Dict[str, dict]:
        """
        Возвращает словарь с данными контакта.
        
        Args:
            ckeys (list, optional): Список ключей полей. По умолчанию msg.cont_keys
            
        Returns:
            Dict[str, dict]: Словарь с данными контакта
        """
        cvalues = [self.count, self.name, self.surn, self.phone, self.note, self.tags, self.created, self.modified]
        return {self.cid : dict(zip_longest(ckeys, cvalues))}


    def add(self, ckeys: list = msg.cont_keys) -> None:
        """
        Добавляет контакт в список.
        
        Args:
            ckeys (list, optional): Список ключей полей. По умолчанию msg.cont_keys
        """
        self.book.update(self.get(ckeys))
        repo.cont_file.save(self.book)


"""Собственно главный объект
список контактов, с которым работаем"""
contacts = ContactList()