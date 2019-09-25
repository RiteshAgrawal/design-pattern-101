from twilio import Twilio

class SMSSender(object):
    def send_sms(self, message, number):
        pass


class TwilioSender(SMSSender):
    def __init__(self):
        self._connection = Twilio()

    def send_sms(self, message, number):
        print('SMS send to {0} via Twilio'.format(number))


if __name__ == '__main__':
    t = TwilioSender()
    t.send_sms('Hello World', '91231231230')
