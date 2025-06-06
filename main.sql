CREATE TABLE IF NOT EXISTS nomnom (
  NAME TEXT,
  NEIGHBOURHOOD TEXT,
  CUISINE TEXT,
  REVIEW REAL,
  PRICE TEXT,
  HEALTH TEXT
);

INSERT INTO nomnom(NAME, NEIGHBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
  ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
  ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
  ('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
  ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
  ('Minca', 'Downtown', 'American', 4.6, '$$$', 'B'),
  ('Riya', 'Mumbai', 'Indian', 4.9, '$$$$$', 'A'),
  ('George', 'Brooklyn', 'Steak', 4, '$$$$', 'A'),
  ('Jasmine', 'Midtown', 'Korean', 3.2, '$$', 'B'),
  ('Priya', 'Midtown', 'Burger', 4, '$$$', 'B'),
  ('Mohan', 'Paris', 'Italian', 4.1, '$$', 'B');

select * from nomnom;

select '---Maximum---';
select max(REVIEW) from nomnom;

select '---Minimum---';
select min(REVIEW) from nomnom;

select '---Average---';
select avg(REVIEW) from nomnom;

select '---Sum---';
select sum(REVIEW) from nomnom;

select '---distinct---';
select distinct(NEIGHBOURHOOD) from nomnom;

select '----------';
select * from nomnom where NEIGHBOURHOOD like ('%n');

select '---AVG REVIEW---';
select CUISINE, avg(REVIEW) from nomnom group by CUISINE;

select '---MAX REVIEW---';
select CUISINE, max(REVIEW) from nomnom group by CUISINE;