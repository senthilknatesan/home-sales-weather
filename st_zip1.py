import sys
import requests
import json
import time

input_file_name =  '/Users/senthilnatesan/Desktop/job-search/sap/ghcnd-stations.txt'
output_file_name = '/Users/senthilnatesan/Desktop/job-search/sap/ghcnd-stations-with_zip.txt'
d = {}
l = []


def load_existing_data ():
    read_file = open(output_file_name, 'r')

    for line in read_file:
        line = line.strip ()
        words = line.split ('|')
        if len(words) < 2:
            continue
        station_id = words[1]
        l.append (station_id)

    read_file.close()
    print l


def make_dict_of_stations():
    with open(input_file_name) as f:
        for line in f:

            line = line.strip()
            words = line.split()

            if ( len(words) < 5 ) :
                print line
                print " number of fields is ", len (words)
                continue;


            if (words[0][0:2] != "US"):
    #            print words[0][0:2], "continue"
                continue

            key = words[0]
            val = words[1] + "|" + words[2]
            d.setdefault(key, val)

def get_zip_for_stations():

    out_file = open(output_file_name, 'a')
    url = 'http://api.geonames.org/findNearbyPostalCodesJSON?'
    for k, v in d.items():
        if (k in l):
            print k
            continue
        v.strip()
        words = v.split('|')
        lat = words[0]
        lon = words[1]
        data = 'lat=' + lat + '&lng=' + lon + '&maxRows=1&username=senthilkn'
        response = requests.get(url + data )
        s = response._content
        j = json.loads(s)
        try:
            z = j['postalCodes'][0]['postalCode']
        except IndexError:
            z = 0
        except KeyError:
            print "going to wait"
            time.sleep (650)
            print "starting again"
            z = 0
        print k, "," , v, ",", z
        o = str(z) + "|" + str(k) + "\n"
        out_file.write (o)

    out_file.close()




def main ():
    load_existing_data ()
    make_dict_of_stations()
    get_zip_for_stations()


if __name__ == '__main__':
    main()


