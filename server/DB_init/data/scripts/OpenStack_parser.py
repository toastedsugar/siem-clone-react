# Parse IBM BlueGene data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "LogRecord",
        "Year",
        "Month",
        "Day",
        "Time",
        "PID",
        "Level",
        "Component",
        "ADDR",
        "Content"
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/OpenStack/OpenStack_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line.split(" ", 6)

        # Split full date into year, month and day
        date = splitline[1].split("-", 2)
        splitline[1] = date[0]                  # Add year
        try: splitline.insert(2, date[1])            # Add month
        except: print(date)
        splitline.insert(3, date[2])            # Add day

        # Split final index into ADDR and Component sections
        temp = splitline[8].partition("]")
        #print(temp)
        splitline[8] = temp[0][1:]
        splitline.append(temp[2])
        
        print(splitline)

        exportData.append(
            [counter] + splitline
        )  # Add the index to data and add it to master list
        

        

        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/OpenStack-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
