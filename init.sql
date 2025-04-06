create schema covid;


create table covid.covid_data (
    ID serial primary key,
    DATE date not null,
    Confirmed integer,
    Recovered integer,
    Deaths integer,
    Increase_Rate numeric);