#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/azureuser/ConnectFour/")

from app import app as application
application.secret_key = '!rkb%fa-qz1f-ln4+m4k@t^-$o88#uph+*uw8l++0)af0-m5l@'
