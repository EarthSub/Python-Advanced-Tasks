from abc import ABC, abstractmethod


class UnderMaintenanceException(Exception):
    pass


class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending email with message: {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")


class PushSender(NotificationSender):
    def send(self, message: str):
        self.is_under_maintenance = True
        raise UnderMaintenanceException('The Push Sender is under maintenance.')


class NotificationService:
    def __init__(self, sender_type: str):
        if sender_type == "email":
            self.sender = EmailSender()
        elif sender_type == "sms":
            self.sender = SMSSender()
        elif sender_type == "push":
            self.sender = PushSender()

    def notify(self, message: str):
        self.sender.send(message)


try:
    email_service = NotificationService("email")
    email_service.notify("Hello via email!")

    sms_service = NotificationService("sms")
    sms_service.notify("Hello via SMS!")

    push_service = NotificationService("push")
    push_service.notify("Hello via Push!")

except UnderMaintenanceException as ex:
    print(ex)
