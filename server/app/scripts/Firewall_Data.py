"""
The purpose of this script is to insert all the data from the 
Firewall data file (log2.csv) into an SQL database where it can 
be consumed by the frontend or used in further data analysis
"""

import csv
import psycopg2

data_path = "../Data/firewall_data.csv"

con = psycopg2.connect(
    database="siem-data",
    user="postgres",
    host="localhost",
    password="postgres",
    port=5432,
)

cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS firewall_data("
    "id SERIAL PRIMARY KEY,"
    "source_port INTEGER,"
    "destination_port INTEGER,"
    "nat_source_port INTEGER,"
    "nat_destination_port INTEGER,"
    "action VARCHAR(12),"
    "bytes INTEGER,"
    "bytes_sent INTEGER,"
    "bytes_recieved INTEGER,"
    "packets INTEGER,"
    "elapsed_time INTEGER,"
    "packets_sent INTEGER,"
    "packets_recieved INTEGER)"
)

with open(data_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    headers = next(csv_reader)  # skip the first line
    line_count = 0

    print("Adding Raw Firewall Data to Database")

    for row in csv_reader:
        cur.execute(
            "INSERT INTO firewall_data ("
            "id, "
            "source_port,"
            "destination_port,"
            "nat_source_port,"
            "nat_destination_port,"
            "action,"
            "bytes,"
            "bytes_sent,"
            "bytes_recieved,"
            "packets,"
            "elapsed_time,"
            "packets_sent,"
            "packets_recieved"
            ") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                line_count,
                row[0],  # source_port,
                row[1],  # destination_port,
                row[2],  # nat_source_port,
                row[3],  # nat_destination_port,
                row[4],  # action,
                row[5],  # bytes,
                row[6],  # bytes_sent,
                row[7],  # bytes_recieved,
                row[8],  # packets,
                row[9],  # elapsed_time,
                row[10],  # packets_sent,
                row[11],  # packets_recieved,
            ),
        )

        # print(row)
        line_count += 1
        print(line_count)


    print(line_count)
con.commit()
