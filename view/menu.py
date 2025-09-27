class Menu:
    @staticmethod
    def show_menu() -> str:
        """Отображение меню и получение команды"""
        return input('Нажмите: \n1 - Показать контакты \n2 - Создать/заменить контакт \n3 - Найти контакт \n4 - Удалить контакт\n')
    
    @staticmethod
    def show_contacts(contacts: dict):
        """Отображение списка контактов"""
        if not contacts:
            print("Список контактов пуст")
            return
            
        for name, data in sorted(contacts.items()):
            print(f'Имя: {name}')
            print(f'Телефон: {data["phone"]}')
            print(f'Доп.инфа: {data.get("comment", "")}')
            print(f'Почта: {data.get("mail", "")}')
            print('-' * 20)

    @staticmethod
    def get_contact_data():
        """Получение данных контакта от пользователя"""
        name = input('Введите имя: ')
        phone = input('Введите номер: ')
        comment = input('Введите доп. информацию: ')
        mail = input('Введите почту: ')
        return name, phone, comment, mail
    
    @staticmethod
    def confirm_action(message: str) -> bool:
        """Подтверждение действия"""
        answer = input(f'{message} (Да/Нет): ')
        return answer.lower() == 'да'
    
    @staticmethod
    def get_search_query() -> str:
        """Получение поискового запроса"""
        return input('Введите желаемый контакт: ')
    
    @staticmethod
    def show_search_results(results: list):
        """Отображение результатов поиска"""
        if results:
            print("Найдены контакты:")
            for result in results:
                print(result)
        else:
            print("Контакт не найден")

    @staticmethod
    def get_contact_to_delete() -> str:
        """Получение имени контакта для удаления"""
        return input('Введите контакт для удаления: ')

    @staticmethod
    def show_message(message: str):
        """Отображение сообщения"""
        print(message)



