import numpy as np
import pandas as pd
import csv
import sqlite3

db_path = "../data.db"
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS firewall_data(source_port INTEGER)")

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


        cur.execute("INSERT INTO firewall_data (source_port) VALUES (?)", (source_port,))
        #print(row)
        line_count += 1
        print(line_count)
        
    con.commit()
        
    print(line_count)