import json

class ContactStorage:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        
    def get_contacts(self) -> dict:
        """Загрузка контактов из файла"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            file_content = file.read().strip()
            if not file_content:
                contacts = {}
            else:
                contacts = json.loads(file_content)
        return contacts 

    def save_contacts(self, contacts: dict):
        """Сохранение контактов в файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)

    def contact_exists(self, name: str) -> bool:
        """Проверка существования контакта"""
        contacts = self.load_contacts()
        return name in contacts

    def get_all_contacts(self) -> dict:
        """Получение всех контактов"""
        return self.get_contacts()