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

    print "Creating table ..."

    # create the table
    query = "CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
    for column in columns:
        name,isnum = column
        name = name.replace(' ','_').replace('-','')
        if name.isdigit():
            name = "Year_{0}".format(name)
        t = "TEXT"
        if isnum:
            t = "INT"
        query += "{0} {1},\n".format(name,t)
    query = query[:-2]
    query += ")"
    #print query
    cur.execute(query)

    print "Loading {0} rows of data ...".format(len(data))

    # load the data
    i = 0
    for row in data:
        query = "INSERT INTO data VALUES("
        if not i == 0:
            for col in row:
                if not col.isdigit():
                    col = '"{0}"'.format(col)
                query += "{0},".format(col)
        i += 1
        query = query[:-1] # last coma
        query += ")"
        #print query
        cur.execute(query)
        print "Done with {0}".format(i)
    
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
