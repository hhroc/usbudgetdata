import csv
import sqlite3

con = None

def readfile(infilename):
    data = []
    i = 0
    with open(infilename,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            r = []
            for col in row:
                r.append(col)
            data.append(r)
        i += 1
    #print i
    return data

def readcolumns(data):
    columns = []
    #print data[1]
    for i in range(0,len(data[0])):
        name = data[0][i]
        if data[1][i].replace('-','').isdigit():
            isnum = True
        else:
            isnum = False
        columns.append((name,isnum))
    return columns

def writedb(columns,data,outputfile):
    con = sqlite3.connect(outputfile)
    cur = con.cursor()

    # create the table
    query = "CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT,"
    for column in columns:
        name,isnum = column
        t = "TEXT"
        if isnum:
            t = "INT"
        query += "{0} {1},".format(name,t)
    query += ")"
    cur.execute(query)

    # load the data
    query = "INSERT INTO data VALUES("
    i = 0
    for row in data:
        if not i == 0:
            for col in row:
                query += "{0},".format(col)
    query = query[:-1] # last coma
    query += ")"
    cur.execute(query)
    
    cur.close()
    con.close()

    return con

def main():
    infilename = "../data/BUDGET-2014-DB-1.csv"
    outfilename = "output.sqlite"
    
    print "Reading data ..."
    data = readfile(infilename)
    
    print "Processing data ..."
    columns = readcolumns(data)
    
    print "Writing out data ..."
    writedb(columns,data,outfilename)
    
    print "Done."

main()
