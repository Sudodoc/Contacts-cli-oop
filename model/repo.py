"""
Модуль для работы с хранилищем данных.
Содержит классы и функции для управления файлами контактов и настроек путей к файлам.
"""

import json
from pathlib import Path
from config import msg


"""Определение пути к корневой директории проекта
"""
BASE_PATH = Path(__file__).resolve().parent.parent

"""Путь к файлу с настройками settings.json
"""
CONF_PATH = BASE_PATH / 'config/settings.json'


class ConfigFileNotFoundError(FileNotFoundError):
    """Кастомное исключение если нет файла settings.json"""
    pass


class ContactsFileNotFoundError(FileNotFoundError):
    """Кастомное исключение если нет файла контактов"""
    pass


class StorageManager:
    """
    Класс для управления файлами хранилища.
    """

    def __init__(self, file_path: Path, isconfig: bool = False):
        """
        Инициализирует менеджер хранилища.
        
        Args:
            file_path (Path): Путь к файлу
            isconfig (bool, optional): Флаг конфигурационного файла. По умолчанию False
        """
        self.path = file_path
        self.isconfig = isconfig

    def open(self) -> dict:
        """
        Открывает и читает файл.
        
        Returns:
            dict: Содержимое файла в виде словаря
            
        Raises:
            ConfigFileNotFoundError: Если не найден конфигурационный файл
            ContactsFileNotFoundError: Если не найден файл контактов
        """
        try:
            with self.path.open('r', encoding='UTF-8') as file:
                return json.load(file)
        except FileNotFoundError:
            if self.isconfig:
                raise ConfigFileNotFoundError(msg.conf_not_found.format(file=self.path))
            else:
                raise ContactsFileNotFoundError(msg.cont_not_found.format(file=self.path))

    def save(self, content: dict) -> None:
        """
        Записывает данные в файл.
        
        Args:
            content (dict): Данные для сохранения
            
        Raises:
            ConfigFileNotFoundError: Если не удалось сохранить конфигурационный файл
            ContactsFileNotFoundError: Если не удалось сохранить файл контактов
        """
        try:
            with self.path.open('w', encoding='UTF-8') as file:
                json.dump(content, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            if self.isconfig:
                raise ConfigFileNotFoundError(msg.no_way_to_save_cont.format(file=self.path))
            else:
                raise ContactsFileNotFoundError(msg.no_way_to_save_cont.format(file=self.path))


'''Файл конфигурации settings.json
'''
conf_file = StorageManager(CONF_PATH, True)

'''Путь к файлу с контактами
'''
cont_path = BASE_PATH / conf_file.open()['default_path']

'''Файл с контактами *.json
'''
cont_file = StorageManager(cont_path)

''''Счётчик
'''
count = conf_file.open()[msg.COUNTER]


if __name__ == '__main__':
    print(BASE_PATH)
    print(CONF_PATH)
    conf = StorageManager(CONF_PATH)
    print(conf.open())
    print(conf.open()['default_path'])
    to_contacts = BASE_PATH / conf.open()['default_path']
    print(to_contacts)
    cl = StorageManager(to_contacts)
    print(cl.open())
