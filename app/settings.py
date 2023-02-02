
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


API_KEY  = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAME', 'sandbox')
URL = os.getenv('URL', 'https://api.sandbox.africastalking.com/version1/messaging')
SHORT_CODE = os.getenv('SHORT_CODE', '7633')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEOAPIFY_API_KEY = os.getenv('GEOAPIFY_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
