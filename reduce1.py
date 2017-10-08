#!/usr/bin/python

import sys

lineNo = 0
input_file_name = '/Users/senthilnatesan/Desktop/job-search/sap/test_file'
output_file_name = '/Users/senthilnatesan/Desktop/job-search/sap/2015-precip'


ct_station_id = -1
precip_sum = 0.0

out_file = open (output_file_name, 'w' )

for line in sys.stdin:
#with open(input_file_name) as f:
#    for line in f:

        lineNo += 1;

        line = line.strip()
        words = line.split('|')


        if ( len(words) < 3 ) :
            print line
            print " number of fields is ", len (words)
            continue;

        next_station_id = words[0]
        next_month = words[1]
        try:
            next_precip = float(words[2])
        except ValueError:
            next_precip = 0.0
            print words[2]

        if (ct_station_id == -1):
            ct_station_id = next_station_id
            ct_month = next_month
            precip_sum += next_precip
            continue

        if ( ct_station_id == next_station_id):
            if (ct_month == next_month):
                precip_sum += next_precip
            else:
                s = ct_station_id + "|" + ct_month + "|" + str(precip_sum) + "\n"
                out_file.write(s)
                precip_sum = next_precip
                ct_month = next_month
        else:
            s = ct_station_id + "|" + ct_month + "|" + str(precip_sum) + "\n"
            out_file.write(s)
            ct_station_id = next_station_id
            ct_month = next_month
            precip_sum = next_precip

out_file.close()

