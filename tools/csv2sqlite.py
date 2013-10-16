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
    print i
    return data

def readcolumns(data):
    columns = []
    for i in range(0,len(data[0])):
        name = data[0][i]
        if '"' in data[1][i] or "'" in data[1][i]:
            isnum = False
        else:
            isnum = True
        columns.append((name,isnum))
    return columns

def createdb(columns,outputfile):
    con = sqlite3.connect(outputfile)
    #CREATE TABLE data
    #cur

def main():
    infilename = "../data/BUDGET-2014-DB-1.csv"
    outfilename = "output.sqlite"
    data = readfile(infilename)
    print data
    columns = readcolumns(data)
    print columns

main()
