from datetime import datetime
import random

def get_formated_datetime():
    timenow = datetime.now()
    return timenow.strftime("%d.%m.%y|%H:%M:%S")


def translit(text):
    charset = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    transtext = []

    for char in text.lower():
        if char in charset:
            transtext.append(charset[char])

        elif char == " ":
            transtext.append("_")

        elif char.isascii():
            transtext.append(char)

        else:
            transtext.append("_")

    return ''.join(transtext)


def random_str(amount=2):
    allchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.sample(allchars, amount))


def get_digits(text):

    digitext = []

    if text.startswith("+"):
        digitext.append(text[0])

    for char in str(text):

        if text == 'x':
            return 'YY'

        elif char.isdigit():
            digitext.append(char)

    return ''.join(digitext)


def gen_id(name, surname, tel, rcount):

    if name == 'N/A':
        name = 'x'
    if surname == 'N/A':
        surname = 'x'
    if tel == 'N/A':
        tel = 'x'

    digitel = get_digits(tel)

    name_part = translit(str(name[0])).upper()
    surname_part = translit(str(surname[0])).upper()
    tel_part = digitel[-2:]

    return str(rcount) + name_part + surname_part + tel_part


if __name__ == "__main__":

    print(random_str())
    print(translit("Семён Семёнович"))
    print(gen_id("Иван", "Иванович", '+79244448990', 1))
