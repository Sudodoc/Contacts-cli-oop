from config import msg
from model.cl import contacts


def option(opt: str, cancel_value=msg.X):
    if opt == cancel_value or (opt.isdigit() and int(opt) in range(1, len(msg.options) + 1)):
        return True
    return False


def confirm(opt: str, ok_value=msg.Y, no_value=msg.N):
    if opt == ok_value or opt == no_value:
        return True
    return False


def mode(opt: str, modify_value=msg.M, delete_value=msg.D, cancel_value=msg.X):
    if opt == modify_value or opt == delete_value or opt == cancel_value:
        return True
    return False


def cid(opt:str, cancel_value=msg.X):
    if opt in contacts.book or opt == cancel_value.upper():
        return True 
    return False


def field(opt:str, detected_id, cancel_value=msg.X):
    if opt in str(contacts.book[detected_id]).lower() or opt == cancel_value:
        return True
    return False


def entry(opt: str | list, cancel_value=msg.X):

    if isinstance(opt, list) and opt[0] == cancel_value:
        return False
    elif opt == '':
        return 'N/A'

    return opt


def phone(opt: str, cancel_value=msg.X):

    if opt == cancel_value:
        return True

    for char in opt:
        if not (char.isdigit() or char in msg.phone_chars):
            return False

    return True

def search(opt: str):
    if opt == '' or opt == ' ':
        return False
    return True

if __name__ == '__main__':

    mlist = ['x']
    print(mlist)

    print(isinstance(mlist, list))