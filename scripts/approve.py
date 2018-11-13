#!/usr/bin/env python2

import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("imageId")
args = parser.parse_args()
imageId = args.imageId

# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("UPDATE `images` SET `imageApproved`= 1 WHERE `imageId`= " + imageId)
db.commit()

# disconnect from server
db.close()
