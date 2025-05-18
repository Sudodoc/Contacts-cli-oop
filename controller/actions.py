from model.cl import SingleContact, contacts
from view import enter, show
from config import msg
from model import cl, repo


def delete(detected_id: str):

    to_delete = enter.confirm(msg.ask.confirm_del)

    if to_delete:
        cl.contacts.remove(detected_id)
        show.alert(msg.del_ok.format(cid=detected_id))



def modify(detected_id: str):
    
    ok, modi_key, new_value = enter.mod_value(detected_id)

    if ok:
        cl.contacts.change(detected_id, modi_key, new_value, msg.MODIFIED)
        show.alert(msg.modify_ok.format(cid=detected_id))



def modify_or_delete(one_id='', ok=True):

    if not one_id:
        ok, detected_id = enter.cid(msg.ask.cid)
    else:
        detected_id = one_id

    if ok:
        show.one_(contacts.book, detected_id)
        ok, action = enter.mod_or_del(msg.ask.m_d_x)

        if ok:
            if action == msg.M:
                modify(detected_id)


            elif action == msg.D:
                delete(detected_id)


def create_contact():

    settings = repo.conf_file.open()
    data, cancel = enter.new_contact(msg.fields_input)
    if cancel: return data
    repo.count += 1
    contact = SingleContact(
        repo.count,
        data[msg.NAME],
        data[msg.SURN],
        data[msg.PHONE],
        data[msg.NOTE],
        data[msg.TAGS],
    )
    contact.add()
    contacts.sync()
    settings[msg.COUNTER] = repo.count
    repo.conf_file.save(settings)
    show.alert(msg.added_ok.format(cid=contact.cid))
    return contact


def global_search():

    search_str = enter.look_up()
    if not search_str:
        return None

    found_contacts = cl.contacts.search(search_str)

    if found_contacts:
        if len(found_contacts) == 1:
            one_id = list(found_contacts.keys())[0]
            modify_or_delete(one_id)

        else:
            show.all_(found_contacts)
            modify_or_delete()

    return global_search()




if __name__ == '__main__':
    # delete('6BZH22')
    # modify('6BZH22')
    print(create_contact().get(msg.cont_keys))