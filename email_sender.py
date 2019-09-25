
from abc import ABC, abstractmethod

from aws import boto3


class BaseEmailSender(ABC):
    def send_email(self, message, to_email):
        pass


class SESEmailSender(BaseEmailSender):
    def send_email(self, message, to_email):
        print('Email send to {0}'.format(to_email))

if __name__ == '__main__':
    s = SESEmailSender()
    s.send_email('hello', 'a@a.com')
