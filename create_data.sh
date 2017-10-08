#!/bin/bash

echo "Creating zip_median_sold_2015.csv zip_median_list_2015.csv "
python  ~/PycharmProjects/hadoop-python-ide/sap1.py

echo "Creating  2015 precipitation file "
cat 2015.csv | python ~/PycharmProjects/hadoop-python-ide/map1.py | sort  | python ~/PycharmProjects/hadoop-python-ide/reduce1.py

echo "creating ghcnd-stations-with_zip.txt file. Since this takes close 2 days to running, this wouldn't be run now"
#python ~/PycharmProjects/hadoop-python-ide/st_zip1.py



