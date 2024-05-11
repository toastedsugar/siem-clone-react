# Parse IBM BlueGene data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "Year",
        "Month",
        "Day",
        "Time",
        "Level",
        "Process",
        "Component",
        "Content"
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/Hadoop/Hadoop_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line.split(" ", 4)


        # Split full date into year, month and day
        date = splitline[0].split("-", 2)

        splitline[0] = date[0]                  # Add year
        splitline.insert(1, date[1])            # Add month
        splitline.insert(2, date[2])            # Add day

        content = splitline[6].split(":", 1)
        splitline[6] = content[0]
        splitline.append(content[1])

        print(splitline)
        
        exportData.append([counter] + splitline)

        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/Hadoop-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
