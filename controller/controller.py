from model.contact import Contact
from model.storage import ContactStorage
from model.exceptions import *
from view import Menu

class ContactController:

    def __init__(self):
        self.storage = ContactStorage()
        self.view = Menu()

    def show_all_contacts(self):
        """Показать все контакты"""
        contacts = self.storage.get_contacts()
        self.view.show_contacts(contacts)

    def create_or_update_contact(self):
        """Создание или обновление контакта"""
        name, phone, comment, mail = self.view.get_contact_data()
        contact = Contact(name, phone, comment, mail)
        
        contacts = self.storage.get_contacts()
        
        if name in contacts:
            if self.view.confirm_action('Заменить данные контакта?'):
                contacts[name] = contact.create_new_contact()
        else:
            if self.view.confirm_action('Создать новый контакт?'):
                contacts[name] = contact.create_new_contact()

        if self.view.confirm_action('Сохранить изменения?'):
            self.storage.save_contacts(contacts)
            self.view.show_message('Данные обновлены')
        else:
            self.view.show_message('Данные не обновлены')

    def search_contact(self):
        """Поиск контакта"""
        query = self.view.get_search_query().lower()
        contacts = self.storage.get_contacts()
        
        results = []
        for name, data in contacts.items():
            if (query in name.lower() or 
                query in data["phone"].lower() or 
                query in data.get("mail", "").lower()):
                results.append(f'Имя: {name}, Телефон: {data["phone"]}')
        
        self.view.show_search_results(results)

    def delete_contact(self):
        """Удаление контакта"""
        name = self.view.get_contact_to_delete()
        contacts = self.storage.get_contacts()
        
        if name in contacts:
            if self.view.confirm_action('Удалить контакт?'):
                del contacts[name]
                self.storage.save_contacts(contacts)
                self.view.show_message('Контакт удален')
        else:
            self.view.show_message('Контакт не найден')

    def run(self):
        """Основной цикл приложения"""
        command = self.view.show_menu()
                
        if command == '1':
            self.show_all_contacts()
        elif command == '2':
            self.create_or_update_contact()
        elif command == '3':
            self.search_contact()
        elif command == '4':
            self.delete_contact()
        else:
            self.view.show_message('Неверная команда')