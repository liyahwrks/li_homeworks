import json

def open_file():
    with open('contacts.json', 'r', encoding='utf-8') as file:
        file_content = file.read().strip()
        if not file_content:
            print("Список контактов пока пуст")
            contacts = {}
        else:
            contacts = json.loads(file_content)
    return contacts

def create_new_contact(name, phone, comment='', mail=''):
    if not ((phone[0] == '+' or phone[0].isdigit()) and phone[1::].isdigit()):
        raise ValueError('Невалидный номер\n')
    if not phone or not name:
        raise ValueError('Невозможно добавить пустой контакт, заполните номер/имя\n')
    
    new_contact = {
        str(name): 
            {
            "phone": str(phone),
            "comment": str(comment),
            "mail": str(mail)
            }
    }
    return new_contact

def add_or_change_contact(new_contact: dict):
    contacts = open_file()
    name = [i for i in new_contact.keys()][0]
    if name in set(i for i in contacts):
        answer = input('Заменить данные контакта? Напиши: Да/Нет\n')
        if answer.lower() == 'да':
            contacts[name] = new_contact[name]
    else: 
        answer = input('Контакта с таким именем еще не существует, создать новый контакт? Напиши: Да/Нет\n')
        if answer.lower() == 'да':
            contacts[name] = new_contact[name]
    return contacts

def show_contacts():
    contacts = open_file()
    for i, j in dict(sorted(contacts.items())).items():
        print(f'Имя: {i},\n телефон: {j["phone"]},\n доп.инфа: {j["comment"]}, почтa: {j["mail"]}')

def delete_contact(name):
    contacts = open_file()
    if name in contacts.keys():
        contacts.pop(name)
        save_contacts(contacts)
    else: print('Контакта с таким именем не существует')

def save_contacts(contacts):
    answer = input('Вы уверенны, что хотите сохранить изменения? Введите: "Да/Нет"\n')
    if answer.lower() == 'да':
        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
        print('Данные обновлены')
    else: print('Данные не обновлены')

def search_contact(user_input):
    contacts = open_file()

    results = []
    
    for name, data in dict(sorted(contacts.items())).items():
        if name.lower() == user_input.lower() \
            or data["phone"].lower() == user_input.lower() \
            or data["phone"].lower() == user_input.lower() \
            or data["mail"].lower() == user_input.lower():
            results.append(f'Имя: {name},\n телефон: {data["phone"]},\n доп.инфа: {data["comment"]}, почтa: {data["mail"]}')

    if results:
        return 'Найдены контакты'+'\n'+'\n'.join(results)
    else:
        return 'Контакт не найден'
    
def menu():
    user_comand = input('Нажмите: \n 1 - Показать контакты \n 2 - Создать/заменить контакт \n 3 - Найти контакт \n 4 - Удалить контакт\n')
    if user_comand == '1':
        show_contacts()
    elif user_comand == '2':
        new_contact = create_new_contact(input('Введите имя\n'), input('Введите номер\n'), input('Введите доп. информацию\n'), input('Введите почту\n'))
        contacts = add_or_change_contact(new_contact)
        save_contacts(contacts)
    elif user_comand == '3':
        result = search_contact(input('Введите желаемый контакт\n'))
        print(result)
    elif user_comand == '4':
        delete_contact(input('Введите контакт, который хотите удалить\n'))
    else:
        print('Невалидная команда, пожалуйста, попробуйте снова')

if __name__ == "__main__":
    menu()