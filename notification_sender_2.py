from email_sender import SESEmailSender
from sms_sender import TwilioSender


class NotificationSender(object):
    def __init__(self, user):
        self.user = user

    def notify(self):
        e = SESEmailSender()
        e.send_email('Hello', self.user.email)

        t = TwilioSender()
        t.send_sms('Hello', self.user.number)


class User(object):
    def __init__(self, number, email):
        self.number = number
        self.email = email


if __name__ == '__main__':
    u = User('1231231230', 'a@a.com')
    n = NotificationSender(u)
    n.notify()

