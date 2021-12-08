import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from rest_framework.response import Response
import pdb
client = Client('AC057eb0fda66b130a042ed7196ba0ffa9', '3c2a08f683130d6037b2ae6d20542c7c')
verify = client.verify.services('VA451b54da0c28392025a024aa83ca51d8')


def send(phone):
    #pdb.set_trace()
    verify.verifications.create(to=phone, channel='sms')


def check(phone, code):
    # pdb.set_trace()
    try:
        result = verify.verification_checks.create(to=phone, code=code)

    except TwilioRestException:
        print('no')
        return False

    return result.status == 'approved'