#!/usr/bin/env python2

import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("userId")
args = parser.parse_args()
userId = args.userId

# Open database connection
db = MySQLdb.connect("localhost","jwadams","oldmanjohnson","it210b")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("DELETE FROM users WHERE userId= " + userId)
db.commit()

# disconnect from server
db.close()
