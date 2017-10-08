select c.zip, c.yyyymm, c.sales_price, c.list_price, c.v2 as discp_percentage,
s.station_id, p.precipitation
from
(select a.zip, a.yyyymm, a.price as sales_price, b.price as list_price, 
((abs(b.price-a.price)/b.price)*100) as v,
((abs(b.price-a.price)/a.price)*100) as v1,
((abs(b.price-a.price)/((a.price + b.price)/2))*100) as v2
from home_sales a, home_listings b
where a.zip = b.zip and
a.yyyymm = b.yyyymm and
a.price <> 0 and
b.price <> 0 
order by v2 desc
limit 1) c, station_zip s, precipitation p
where c.zip = s.zip and
s.station_id = p.station_id and
c.yyyymm = p.yyyymm;

