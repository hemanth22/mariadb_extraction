import mysql.connector as mysql
import os
import sys
import csv

databasename = os.environ['databasename']
databasehost = os.environ['databasehost']
databaseusername = os.environ['databaseusername']
databasepassword = os.environ['databasepassword']
databaseport = os.environ['databaseport']

def connect(db_name, dbhost, dbuser, dbpass, dbport):
    try:
        return mysql.connect(
            host=dbhost,
            user=dbuser,
            password=dbpass,
            database=db_name,
            port=dbport)
    except Error as e:
        print(e)

if __name__ == '__main__':
    db = connect(databasename,databasehost,databaseusername,databasepassword,databaseport)
    f = open("test.csv", "w")
    cursor = db.cursor()
    fields = ['id', 'ask', 'bid', 'creationdate'] # field names 
    dbquery = "SELECT `id`, `ask`, `bid`, `creationdate` FROM `publishedrates`" # query
    cursor.execute(dbquery)
    project_records = cursor.fetchall() # fetch all records
    outputfile = csv.writer(f, lineterminator='\n') # create the csv writer object
    outputfile.writerow(fields) # write the fields
    outputfile.writerows(project_records) # write the data
    print(project_records)
    db.close()
