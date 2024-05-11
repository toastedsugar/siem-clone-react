CREATE TABLE IF NOT EXISTS Linux_Data (
    LineId int,
    Month varchar(3), 
    Date int, 
    Time time,
    Level varchar(5),
    Component text,
    PID int,
    Content text,
    EventId varchar(4),
    EventTemplate text
);

COPY Linux_Data
FROM '/docker-entrypoint-initdb.d/data/loghub-data-raw/Linux/Linux_2k.log_structured.csv'
DELIMITER ','
CSV HEADER;