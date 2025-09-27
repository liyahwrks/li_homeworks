from typing import Optional
from model import InvalidPhoneError, InvalidMailError

class Contact:
    def __init__(self, name: str, phone: str, comment: Optional[str], mail: Optional[str], **kwargs) -> None:
        self.name = name 
        self.phone = phone 
        self.comment = comment
        self.mail = mail

    def _validate_phone(self):
        if not ((self.phone[0] == '+' or self.phone[0].isdigit()) and self.phone[1::].isdigit()):
            raise InvalidPhoneError(self.phone)
        
    def _validate_mail(self):
        if self.mail:
            if not (self.mail.endswith('.ru') or self.mail.endswith('.com')):
                raise InvalidMailError(self.mail)
        
    def create_new_contact(self):

        self._validate_phone()
        self._validate_mail()
        
        new_contact = {
            "phone": str(self.phone),
            "comment": str(self.comment),
            "mail": str(self.mail)
        }
        return new_contact