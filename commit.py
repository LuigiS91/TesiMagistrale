#!/usr/bin/python3.7

from datetime import datetime
import os


now = datetime.now()
commit_name = '"Aggiornamento : '+now.strftime("%d/%m/%Y %H:%M:%S"+'"')

os.system("git commit -am "+ commit_name)
os.system("git push")