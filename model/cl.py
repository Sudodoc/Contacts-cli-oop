from typing import Dict
from config import msg
from pathlib import Path
from model import repo, utils
from itertools import zip_longest


class ContactList:

    def __init__(self,
                 cont_dict: Dict[str, dict] = repo.cont_file.open(),
                 cont_path: Path = repo.cont_path
                 ):
        self.book = cont_dict
        self.path = cont_path

    def remove(self, detected_id: str):
        del self.book[detected_id]
        repo.cont_file.save(self.book)

        
    def change(self, detected_id: str, modi_key: str, new_value: str, time_key: str):
        self.book[detected_id][modi_key] = new_value
        self.book[detected_id][time_key] = utils.get_formated_datetime()
        repo.cont_file.save(self.book)


    def search(self, search_str: str, no_result=msg.no_result):
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

    def sync(self):
        self.book = repo.cont_file.open()
        print('sync book')


class SingleContact(ContactList):

    def __init__(self, c_count, c_name, c_surn, c_phone, c_note, c_tags, modified=None,
                 cont_dict: Dict[str, dict] = repo.cont_file.open(),
                 cont_path: Path = repo.cont_path
                 ):

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

    def get(self, ckeys: list = msg.cont_keys):

        cvalues = [self.count, self.name, self.surn, self.phone, self.note, self.tags, self.created, self.modified]
        return {self.cid : dict(zip_longest(ckeys, cvalues))}

    def add(self, ckeys: list = msg.cont_keys):
        self.book.update(self.get(ckeys))
        repo.cont_file.save(self.book)


"""Собственно главный объект
список контактов, с которым работаем"""
contacts = ContactList()