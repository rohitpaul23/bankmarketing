import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very_tough_to_guess'
    