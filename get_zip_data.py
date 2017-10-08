import sys
import logging
import pymysql
import mysql_config
import json


def get_zip_data (event_obj, context):

    print event_obj
    zip = event_obj['zip']
    print "zip is ", zip

    rds_host = mysql_config.sql_endpoint
    name = mysql_config.sql_username
    password = mysql_config.sql_password
    db_name = mysql_config.db_name

    if (len(zip)) != 5:
        return ({zip: 'Invalid input'})

    try:
        izip = int(zip)
    except:
        return ({zip: 'Invalid input'})

    if (izip < 0 or izip > 99999):
        return ({zip: 'Invalid input'})

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        print ("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    sa = {}
    sa['zip'] = zip
    sa['year'] = 2015

    with conn.cursor() as cur:
        s = 'select yyyymm, price from home_sales a where a.zip = ' + zip
        cur.execute(s)
        sd = {}
        for row in cur:
            yyyymm, price = row
            sd[yyyymm] = price

        sa['sales'] = sd

        s = 'select yyyymm, price from home_listings a where a.zip = ' + zip
        cur.execute(s)
        sd = {}
        for row in cur:
            yyyymm, price = row
            sd[yyyymm] = price

        sa['listing'] = sd

        s = "select a.station_id, b.yyyymm, b.precipitation from station_zip a, precipitation b where a.station_id = b.station_id and a.zip = " + str(zip)
        cur.execute(s)
        sl = []
        for row in cur:
            sd = {}
            station_id, yyyymm, precip = row
            sd['station_id'] = station_id
            sd['yyyymm'] = yyyymm
            sd['precipitation'] = precip
            sl.append (sd)

        sa['station_info'] = sl

        if ((not sa['listing']) and (not sa['sales']) and not (sa['station_info'])):
            return ({zip: 'No data found'})

    return sa

if __name__ == '__main__':

    if  len (sys.argv) <> 1:
        print "usage: get_zip_data.py"
        exit (1)

    context = ''

    event_json = '{ "zip": "60103" }'

    event_obj = json.loads (event_json)

    rd = get_zip_data (event_obj, context)

    print rd



