class InvalidPhoneError(Exception):
    def __init__(self, phone, message=" - невалидный номер"):
        self.number = phone
        self.message = str(phone) + message
        super().__init__(self.message)

class InvalidMailError(Exception):
    def __init__(self, mail, message=" - невалидный мейл"):
        self.mail = mail
        self.message = str(mail) + message
        super().__init__(self.message)