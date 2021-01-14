#!/usr/bin/python3.6
activate_this = '/var/www/www-root/data/www/liontracts.ru/FlaskApp/FlaskApp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/www-root/data/www/liontracts.ru/FlaskApp/FlaskApp")
from FlaskApp import app as app
# application.secret_key = 'Add your secret key'