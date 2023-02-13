from os import environ
from dotenv import load_dotenv, find_dotenv


def dotenv_path():
    return find_dotenv()


def chrome_driver_path():
    return dotenv_path().replace('.env', 'chromedriver')


load_dotenv(dotenv_path())


# Facebook APP
APP_ID = environ['APP_ID']
APP_SECRET = environ['APP_SECRET']


# Facebook OAuth
STATE = environ['STATE']
REDIRECT_URI = environ['REDIRECT_URI']
OAUTH_URL = f'https://www.facebook.com/v16.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&state={STATE}'


# Selenium
EMAIL = environ['EMAIL']
PASSWORD = environ['PASSWORD']


# Server
SEC_CODE = environ['SEC_CODE']
SERVER_URL = environ['SERVER_URL']
