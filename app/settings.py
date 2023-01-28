from os import environ
API_KEY  = environ.get('API_KEY')
USERNAME = environ.get('USERNAME', "sandbox")
URL = environ.get('URL', 'https://api.sandbox.africastalking.com/version1/messaging')
SHORT_CODE = environ.get('SHORT_CODE', '7633')
