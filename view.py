
def GetNumber(message, min_number=0, max_number=1):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if number in range(min_number, max_number+1):
                isCorrect = True
            else:
                print(f'Значение должно быть от {min_number} до {max_number}')
        except ValueError:
            print("Введено не целое число. Повторите ввод ")
    return number


def Show_main_menu():
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    menu_items = len(menu_list)
    user_input = GetNumber('Выберите пункт меню: ', 1, menu_items)
    return user_input


def Show_contacts(contacts: list):
    DrawHeading(contacts)
    for contact in contacts:
        for key, value in contact.items():
            if key != 'phone':
                print(f'{value:<15}', end='|')
            else:
                phone_dict = contact.get('phone', "")
                first_number = True
                for number, comment in phone_dict[0].items():
                    if first_number:
                        print(f'{number:15}|{comment}')
                        first_number = False
                    else:
                        print(5*'               |' +
                              f'{number:15}|{comment}')
                DrawLine()


def DrawLine():
    for i in range(7):
        if i != 6:
            print(15*'-', end='+')
        else:
            print(15*'-')


def DrawHeading(contacts: list):
    header_list = ["ИД",
                   "Имя",
                   "Отчество",
                   "Фамилия",
                   "Телефон",
                   "Комментарий"]
    for item in header_list:
        print(f'{item:15}', end='|')
    for i in range(7):
        if i == 0:
            print('\n'+15*'-', end='+')
        elif 0 < i < 6:
            print(15*'-', end='+')
        else:
            print(15*'-')


def CreateContact():
    print('Создание нового контакта...')
    name = input('Имя: ').capitalize().strip()
    surName = input('Отчество: ').capitalize().strip()
    lastName = input('Фамилия: ').capitalize().strip()
    dateOfBirth = input('Дата рождения: ').strip()
    phones = PhonesCreator()
    data = name, surName, lastName, dateOfBirth, phones
    return data


def PhonesCreator():
    phones = {}
    is_quit = False
    while not is_quit:
        key = input('Введите номер телефона: ')
        value = input(
            'Введите комментарий к номеру: ').capitalize().strip()
        phones[key] = value
        is_quit = True if GetNumber(
            'Чтобы добавить другой номер нажмите 1, иначе 0: ') == 0 else False
    return [phones]


def Show_alert(message):
    print(message)


def Show_replace_menu():
    print('Что необходимо изменить?')
    menu_list = ['Изменить имя',
                 'Изменить отчество',
                 'Изменить фамилию',
                 'Изменить дату рождения',
                 'Изменить телефон',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    menu_items = len(menu_list)
    user_input = GetNumber('Выберите пункт меню: ', 1, menu_items)
    return user_input


def Find_contact_input(item: int):
    item_dict = {1: ["name", "Имя"],
                 2: ["surName", "Отчество"],
                 3: ["lastName", "Фамилия"],
                 4: ["dateOfBirth", "Дата рождения"],
                 5: ["phone", "Телефон"]}

    selection = item_dict[item]
    to_find = input(f"Введите {selection[1]}: ")
    return selection[0], to_find


def Select_id(data):
    id_list = []
    isCorrect = False
    for contact in data:
        id_list.append(str(contact["userId"]))
    while not isCorrect:
        id = (
            input(f'Введите id редактируемой записи ({", ".join(id_list)}):'))
        if id in id_list:
            isCorrect = True
        else:
            print(f"Введите число из диапазона {', '.join(id_list)}")
    return int(id)


def show_change_contact(id: int, input_key, contacts: list):
    changed_contact = {}
    for contact in contacts:
        if contact["userId"] == id:
            for key, value in contact.items():
                changed_contact["userId"] = contact["userId"]
                if key != "phone" and key != "userId":
                    if key == input_key:
                        new_value = input(
                            f'Введите новое значение для {key}:{value} (Enter - пропустить)-> ').capitalize().strip()
                        if len(new_value) != 0:
                            changed_contact[key] = new_value
                    else:
                        changed_contact[key] = value
                elif key == input_key == "phone":
                    new_phone = change_phone(contact[key])
                    changed_contact[key] = new_phone
                else:
                    changed_contact[key] = value
    return changed_contact


def change_phone(phones: list):
    contact_phones = phones[0]
    for phone, comment in contact_phones.items():
        new_key = input(
            f'Введите новое значение для {phone}:{comment} (Enter - пропустить)-> ').strip()
        if len(new_key) != 0:
            del contact_phones[phone]
            new_value = input(
                f'Введите новый комментарий для {new_key}: ').strip()
            contact_phones[new_key] = new_value
            phones.pop(0)
            phones.append(contact_phones)
        return phones


def change_alert(key, value, contact):
    do_it = False
    while not do_it:
        result = input(f'Заменить {value} на {contact[key]}? (Y/N): ').upper()
        if result in ('YN'):
            do_it = True
            return True if result == 'Y' else False


def save_alert(compare):
    if not compare:
        print('Данные изменились')
        do_it = False
        while not do_it:
            save = input('Сохранить изменения (Y/N)').upper()
            if save in ('YN'):
                do_it = True
                return True if save == 'Y' else False
