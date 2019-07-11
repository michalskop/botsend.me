#!/usr/bin/python3
activate_this = '/var/www/botsend.me/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)
sys.path.insert(0, "/var/www/botsend.me/")

from botsendme import app as application
