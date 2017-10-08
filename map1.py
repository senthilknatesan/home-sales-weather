#!/usr/bin/python

import sys

lineNo = 0
input_file_name = '/Users/senthilnatesan/Desktop/job-search/sap/2015.csv'

for line in sys.stdin:
#with open(input_file_name) as f:
#    for line in f:

        lineNo += 1;

        line = line.strip()
        words = line.split(',')

        outString = '';
        fieldSep = '|';

        if ( len(words) < 7 ) :
            print " number of fields is ", len (words)
            continue;


        if (words[0][0:2] != "US"):
            continue

        if (words[1][0:4] != "2015" ):
            continue

        if (words[2] != "PRCP" ):
            continue

        key = words[0] + "|" + words[1][0:4] + "-" + words[1][4:6] + "|" + words[3]

        print key

