from config import msg
from model.cl import contacts
from view import show, enter
from controller import actions

def run():

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