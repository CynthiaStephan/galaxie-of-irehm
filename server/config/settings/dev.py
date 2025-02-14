from .base import *

DEBUG = True
CURRENT_IP = '0.0.0.0'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'nginx', CURRENT_IP]
INTERNAL_IPS = ALLOWED_HOSTS
