import json


def Read_file(file) -> list:
    
    try:
        with open(file, "r", encoding='utf-8') as data_file:
            data_from_db = json.load(data_file)
    except FileNotFoundError:
        print('Файл не существует. Выберите создать контакт')
    return data_from_db


def Save_file(contacts_data, file, save_change = True):
    if save_change:
        if contacts_data != Read_file(file):
            with open(file, "w", encoding='utf-8') as data_file:
                json.dump(contacts_data, data_file, indent=2, ensure_ascii=False)
            
    return


def Create_Contact(data, contacts: list):
    name, surName, lastName, dateOfBirth, phones = data
    id = FindLastID(contacts) +1
    new_contact = {"userId":id,
                "name": name.capitalize().strip(),
                   "surName": surName.capitalize().strip(),
                   "lastName": lastName.capitalize().strip(),
                   "dateOfBirth": dateOfBirth.capitalize().strip(),
                "phone": phones}
    contacts.append(new_contact)
    return


def Check_New_Contact(data, contacts: list):
    name, surName, lastName, dateOfBirth, phones = data
    new_contact = name, surName, lastName, dateOfBirth
    new_contact_set = set(new_contact)
    contact_set = set()
    contact_is_present = False
    for contact in contacts:
        for key, value in contact.items():
                isID = (key == 'userId')
                isPhone = (key=='phone')
                if not isPhone and not isID:
                    print(key)
                    print(value)
                    contact_set.add(value)
                elif isPhone:
                    phone_is_present =Check_New_Phones(phones, contact)
        contact_is_present = (new_contact_set == contact_set) or phone_is_present
        if contact_is_present == True: return True
    return False


def Check_New_Phones(phones: list, contact: dict):
    new_phone_set = set(number for number in phones[0].keys())
    phone_set = set(x for x in contact["phone"][0].keys())
    return (new_phone_set == phone_set)
    







def Delete_contact(id, contacts):
    contact = [contacts.index(x) for x in contacts if x["userId"] == id]
    if contact[0] >=0:
        contacts.pop(contact[0])
        print(f'Контакт с id {id} удален')
    return




def FindLastID(data):
    if len(data) > 0:
        maxId = data[0]["userId"]
        for item in data:
            if item["userId"] > maxId:
                maxId = item["userId"]
        return maxId
    else:
        return 0
    
def Find_contact(key, value, contacts: list):
    found_contacts = []
    for contact in contacts:
        if contact[key] == value or value in contact["phone"][0].keys():
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        return 0
    return found_contacts

def change_data(id, contact, data: list, do_change):
    if do_change:
        for i in range(len(data)):
            if data[i]["userId"] == id:
               
                del data[i]
                data.insert(i, contact)

def compare_data(file, data):
    try:
        with open(file, "r", encoding='utf-8') as data_file:
            data_from_db = json.load(data_file)
    except FileNotFoundError:
        print('Файл не существует. Выберите создать контакт')
        if len(data_from_db) == len(data):
            for i in range(len(data)-1):
                if data[i] != data_from_db[i]: return False
            return True
        else: return False

