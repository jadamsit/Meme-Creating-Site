#!/usr/bin/env python2

import MySQLdb
import argparse
import urllib
import urllib2
from PIL import Image
import os

class reg(object):
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row) :
            setattr(self, attr, val)

parser = argparse.ArgumentParser()
parser.add_argument("imageId")
args = parser.parse_args()
imageId = args.imageId

# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `images` WHERE imageId= " + imageId)

# disconnect from server
db.close()

#Find out the filepath
for row in cursor.fetchall():
    r = reg(cursor, row)
    imagePath = r.imagePath

#Remove file from server
os.remove("/home/webadmin/node/assets" + imagePath)

# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("DELETE FROM images WHERE imageId= " + imageId)
db.commit()

# disconnect from server
db.close()
