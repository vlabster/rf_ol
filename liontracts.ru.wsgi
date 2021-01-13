#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/www-root/data/www/liontracts.ru")
from liontracts.ru import app as application
