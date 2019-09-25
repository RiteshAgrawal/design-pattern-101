from aws import boto3
from twilio import Twilio


class NotificationSender(object):
    def __init__(self, user):
        self.user = user

    def notify(self):
       b = boto3()
       b.send_email(self.user.email, 'from@a.com', 'Hello')

       t = Twilio()
       t.send_sms(self.user.number, 'Hello')

       t.call(self.user.number, 'Hello')


class User(object):
    def __init__(self, number, email):
        self.number = number
        self.email = email


if __name__ == '__main__':
    u = User('1231231230', 'a@a.com')
    n = NotificationSender(u)
    n.notify()

