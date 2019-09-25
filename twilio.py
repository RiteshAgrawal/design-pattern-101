class Twilio(object):
    def send_sms(self, number, message):
        print("Message sent to {0}".format(number))

    def call(self, number, message):
        print("Call done to {0}".format(number))
