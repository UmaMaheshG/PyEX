__author__ = 'ugunipati'

import csv
import os

def getLine(filePath):
    filepath = os.path.abspath(filePath)
    f = open(filepath)
    lines=csv.reader(f)

    for line in lines:
        print line
    return line
    f.close()



if __name__=='__main__':
    line = getLine("D:\\platformqjaf\\code\\results\\JmeterDetailSummary\\AggregateCSVAll.csv")

    for val in line:
        print val[1]