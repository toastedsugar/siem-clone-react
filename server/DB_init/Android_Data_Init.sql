CREATE TABLE IF NOT EXISTS Android_Data (
    LineId int,
    Date varchar(4),
    Time varchar(12),
    PID,
    TID,
    Level,
    Component,
    Content
);

COPY Android_Data
FROM '/docker-entrypoint-initdb.d/data/loghub-data-raw/Android/Android_2k.log_structured.csv'
DELIMITER '|'
CSV HEADER;