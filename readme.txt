############# The answer to the question is
zip, yyyy-mm, sales_price, list_price, discrepency_%, station_id, precipitation
81632,2015-02,559423.0,1895000.0,108.83021414732164,US1COEG0003,206.0


#######  There is a service restapi post running to get data for a given zip code
curl -H "x-api-key:sL5KotBPfF7hwYSWcXZPY5d2Q5fMcMzH9irZFCkG" -H "Content-Type: application/json" -X POST -d "{\"zip\": \"80232\"}" https://38urjn046h.execute-api.us-east-1.amazonaws.com/sap21/testing

# sample output below.

#######  source code is attached.
# There is no ec2. The archiecture uses api gateway, lambda and mysql. The python programs were executed from my mac and they are all attched.
# I connected dbvisualizer to mysql to run any sql command. 

######### Improvments could be done but didn't do for the prototype to save money 
1. redshift instead of mysql (free tier). 
2. map reduce streaming model (map and reduce) but ran on mac.
3. Minimum amount of data loaded into mysql
4. Minimum amount of overall testing and no unit testing. Bad Senthil. :-(

############# questions
1. Not sure what average median means? so took the files Zip_MedianListingPrice_AllHomes.csv and Zip_MedianSoldPrice_AllHomes.csv

############ formuala used tp compute the discrepency percentage betwwen average median list and average median sold price is
((abs (list price - sales price ))/ avarageof (list price, sale price)) * 100


############# The output json for the service is as follows
{

"station_info": 
   [	{"yyyymm": "2015-01", "precipitation": 166.0, "station_id": "US1COJF0179"}, 
 	{"yyyymm": "2015-02", "precipitation": 981.0, "station_id": "US1COJF0179"}, 
......
   ],
"listing": 
{
"2015-06": 0.0, "2015-07": 0.0, "2015-04": 0.0, "2015-05": 0.0, "2015-02": 0.0, "2015-03": 0.0, "2015-01": 0.0, "2015-08": 0.0, "2015-09": 0.0, "2015-11": 0.0, "2015-10": 0.0, "2015-12": 0.0
}, 
"sales": 
{
"2015-06": 275550.0, "2015-07": 283450.0, "2015-04": 243037.0, "2015-05": 268700.0, "2015-02": 245073.0, "2015-03": 256536.0, "2015-01": 255400.0, "2015-08": 283500.0, "2015-09": 280000.0, "2015-11": 250050.0, "2015-10": 276500.0, "2015-12": 278285.0
}, 
"zip": "80232", 
"year": 2015
}


