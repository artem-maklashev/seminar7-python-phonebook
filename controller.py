import view
import model


def Menu_selection(item: int):
    match item:
        case 1:
            if len(contacts_data) != 0:
                view.Show_contacts(contacts_data)
            else:
                view.Show_alert('Файл пустой или не существует')
        case 2:
            model.Save_file(contacts_data, file)
        case 3:
            new_data = view.CreateContact()
            contact_is_present = model.Check_New_Contact(
                new_data, contacts_data)
            if not contact_is_present:
                model.Create_Contact(new_data, contacts_data)
            else:
                view.Show_alert('Контакт или телефон уже присутствует')
        case 4:
            replace_selection = view.Show_replace_menu()
            key, value = view.Find_contact_input(replace_selection)
            replace_contact_data = model.Find_contact(
                key, value, contacts_data)
            if replace_contact_data == 0:
                view.Show_alert(f'Контакт {value} не найден')
            else:
                view.Show_contacts(replace_contact_data)
                change_id = view.Select_id(replace_contact_data)
                new_contact_data = view.show_change_contact(
                    change_id, key, contacts_data)
                do_change = view.change_alert(key, value, new_contact_data)
                model.change_data(change_id, new_contact_data,
                                  contacts_data, do_change)
        case 5:
            view.Show_contacts(contacts_data)
            id_delete = view.Select_id(contacts_data)
            new_data = model.Delete_contact(id_delete, contacts_data)
        case 6:
            compare = model.compare_data(file, contacts_data)
            save_change = view.save_alert(compare)
            model.Save_file(contacts_data, file, save_change)
            exit()

file = "bd.json"
contacts_data = model.Read_file(file)

def start():
    while True:
        print('\n')
        user_selection = view.Show_main_menu()
        Menu_selection(user_selection)
