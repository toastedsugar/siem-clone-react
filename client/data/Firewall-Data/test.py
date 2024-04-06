'''
The purpose of this script is to insert all the data found in the Firewall data file (log2.csv)
into an SQL database where it can then be consumed by the frontend or used in further data analysis
'''

import csv
import sqlite3

db_path = "../data.db"
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS firewall_data("
            "source_port INTEGER,"
            "destination_port INTEGER,"
            "nat_source_port INTEGER,"
            "nat_destination_port INTEGER,"
            "action VARCHAR(5),"
            "bytes INTEGER,"
            "bytes_sent INTEGER,"
            "bytes_recieved INTEGER,"
            "packets INTEGER,"
            "elapsed_time INTEGER,"
            "packets_sent INTEGER,"
            "packets_recieved INTEGER)"
            )

with open("log2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    print("Adding Raw Firewall Data to Database")
    
    for row in csv_reader:
        source_port = row[0]
        destination_port = row[1]
        nat_source_port = row[2]
        nat_destination_port = row[3]
        action = row[4]
        bytes = row[5]
        bytes_sent = row[6]
        bytes_recieved = row[7]
        packets = row[8]
        elapsed_time = row[9]
        packets_sent = row[10]
        packets_recieved = row[11]

        cur.execute("INSERT INTO firewall_data ("
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
                    ") VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", 
                    (source_port,
                        destination_port,
                        nat_source_port,
                        nat_destination_port,
                        action,
                        bytes,
                        bytes_sent,
                        bytes_recieved,
                        packets,
                        elapsed_time,
                        packets_sent,
                        packets_recieved,
        ))

        #print(row)
        line_count += 1
        print(line_count)
        
    con.commit()
        
    print(line_count)
