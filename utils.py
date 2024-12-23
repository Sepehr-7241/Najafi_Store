from kavenegar import *


def send_otp_code(phone_number, code):
    api = KavenegarAPI('')
    params = {'sender': '',
              'receptor': phone_number,
              'message': f'کد تایید شما: {code}',
              }
    response = api.sms_send(params)
