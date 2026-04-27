class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return f"Email sent -> {self.message}"


class SMSNotification(Notification):
    def send(self):
        return f"SMS sent -> {self.message}"