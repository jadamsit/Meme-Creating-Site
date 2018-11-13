#!/usr/bin/env python2

import ConfigParser
import os
import time
import getpass

user = "jwadams"

password = "oldmanjohnson"

host = "localhost"

database = "it210b"

filestamp = time.strftime('%Y-%m-%d-%I:%M')
pathname = database+"_"+filestamp+".gz"
destination = '/home/webadmin/backups/database/it210b.gz'
os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (user,password,host,database,database+"_"+filestamp))
os.rename(pathname, destination)

#/home/webadmin/node/scripts/backupdb.py
#/home/webadmin/node/scripts/backupImages.py
