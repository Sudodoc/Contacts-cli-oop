from dataclasses import dataclass


'''Определяем клавишы
'''
X = 'x'
Y = 'y'
N = 'n'
M = 'm'
D = 'd'


'''Определяем кастомные названия полей для словарей
'''
ID = 'cid'
TAGS = 'tags'
PHONE = 'phone'
NUMBER = 'number'
NAME = 'name'
SURN = 'surname'
NOTE = 'comment'
CREATED = 'created'
MODIFIED = 'modified'

cont_keys = [NUMBER, NAME, SURN, PHONE, NOTE, TAGS, CREATED, MODIFIED]

COUNTER = 'counter' #Это для счетчика в настройках

'''Определяем пункты главного меню
'''
options = [
    "Show all",
    "Add new",
    "Search",
]

opt         = "\n\t--- Options ---\n\t"
esc         = "\t[x] Exit"
select_opt  = "\nSelect option: "


'''Определяем символы для проверки номера тел.
'''
phone_chars = (
    '+',
    '-',
    '(',
    ')',
    ' ',
)


'''Системные сообщения
'''
input_err = "Input error, please try again!"
id_err = "No such ID found! Please try again"
field_err = "No such a field! Please try again."
phone_format_err = "invalid phone format"
del_ok = "Contact ID: {cid} has been deleted successfully!"
modify_ok = "Contact ID : {cid} has been updated successfully!"
added_ok = "Contact ID: {cid} has been added successfully!"
search_text = "Insert string for global search or [x] to cancel"
no_result = "Nothing found"
bye = "Contacts-cli is closed!"
conf_not_found = "Config file not found {file}"
cont_not_found = "Contact file not found {file}"
no_way_to_save_conf = "No file {file} found to write data settings"
no_way_to_save_cont = "No file {file} found to write data contacts"


'''Сообщения запросов данных
'''
@dataclass
class AskData:
        confirm_del: str
        phone: str
        name: str
        surn: str
        note: str
        tags: str
        mode: str
        field: str
        value: str
        cid : str
        m_d_x : str
        search : str

ask = AskData(
    confirm_del = "\nAre you sure you want to delete this contact? [Y]/[n]: ",
    phone = "\nEnter phone number or [x] to cancel: ",
    name = "\nEnter name: ",
    surn = "\nEnter surname: ",
    note = "\nEnter any additional notes: ",
    tags = "\nEnter tags, separated by spaces: ",
    mode = "Press [m] to modify, or [d] to delete, or [x] to cancel: ",
    field = "\nEnter field to modify or [x] to cancel: ",
    value = "\nEnter new value or [x] to cancel: ",
    cid = "\nEnter contact ID number to modify/delete or [x] to go back to options: ",
    m_d_x = "Press [m] to modify, or [d] to delete, or [x] to cancel: ",
    search = "\nSearch: "
)


'''Определяем запрашиваемые поля контакта
'''
fields_input = {
    PHONE : ask.phone,
    NAME : ask.name,
    SURN : ask.surn,
    NOTE : ask.note,
    TAGS : ask.tags,
}