select count(*) from srcdata.credits;
select count(*) from srcdata.keywords;
select count(*) from srcdata.links;
select count(*) from srcdata.movies_metadata;
select count(*) from srcdata.ratings;


select * from srcdata.credits limit 20;
select * from srcdata.keywords limit 20;
select * from srcdata.links limit 20;
select * from srcdata.movies_metadata limit 20;
select * from srcdata.ratings limit 20;

select column_name, data_type, character_maximum_length, column_default, is_nullable
from INFORMATION_SCHEMA.COLUMNS where table_name = '<name of table>';

select
    table_schema
    , table_name
    , column_name
    , data_type
    , character_maximum_length
    , column_default
    , is_nullable
FROM 
   information_schema.columns
WHERE 
   table_name = 'credits';

alter table 