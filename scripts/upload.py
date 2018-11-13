#!/usr/bin/env python2

import MySQLdb
import urllib
import urllib2
from PIL import Image

#not my class! Found online!
class reg(object):
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row) :
            setattr(self, attr, val)

basewidth = 500
iss = "192.168.101.136"
# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `images` WHERE uploaded=0")

# disconnect from server
db.close()

for row in cursor.fetchall():
    r = reg(cursor, row)
    urllib.urlretrieve("http://" + iss + r.imagePath, "assets" + r.imagePath)
    img = Image.open("assets" + r.imagePath)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save("assets" + r.imagePath)

# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("UPDATE images SET uploaded=1")
db.commit()

# disconnect from server
db.close()
