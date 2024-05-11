CREATE TABLE IF NOT EXISTS Thunderbird_Data (
    LineId serial,
    Timestamp varchar(10),
    Date varchar(10),
    "User" varchar(12),     -- User is a reserved keyword in sql
    Month varchar(3),
    Day integer,
	Time time,
	Location text,	
    Component text,
    PID	int,
    Content text
);

COPY Thunderbird_Data
FROM '/docker-entrypoint-initdb.d/data/cleaned-data/thunderbird-clean.csv'
DELIMITER '|'
CSV HEADER;