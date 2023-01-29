import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAME', 'sandbox')
URL = os.getenv('URL', 'https://api.sandbox.africastalking.com/version1/messaging')
SHORT_CODE = os.getenv('SHORT_CODE', '7633')

