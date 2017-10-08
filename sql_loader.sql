drop table station_zip;
drop table precipitation;
drop table home_listings;
drop table home_sales;

CREATE TABLE home_sales(
   Zip VARCHAR (10)     NOT NULL,
   yyyymm  varchar (10) NOT NULL, 
   price  float              NOT NULL,
   PRIMARY KEY (zip, yyyymm)
);

CREATE TABLE home_listings(
   Zip VARCHAR (10)     NOT NULL,
   yyyymm  varchar (10) NOT NULL, 
   price  float              NOT NULL,
   PRIMARY KEY (zip, yyyymm)
);


create table precipitation (
 station_id varchar(20) not null,
 yyyymm  varchar (10) NOT NULL, 
 precipitation double,
 primary key (station_id, yyyymm )
);

create table station_zip(
zip varchar(10) not null,
station_id varchar(20) not null,
primary key (station_id )
);



load data local infile '/Users/senthilnatesan/Desktop/job-search/sap/zip_median_sold_2015.csv' into table home_sales fields terminated by ',';
load data local infile '/Users/senthilnatesan/Desktop/job-search/sap/zip_median_list_2015.csv' into table home_listings fields terminated by ',';
load data local infile '/Users/senthilnatesan/Desktop/job-search/sap/2015-precip' into table precipitation fields terminated by '|';
load data local infile '/Users/senthilnatesan/Desktop/job-search/sap/ghcnd-stations-with_zip.txt' into table station_zip fields terminated by '|';


