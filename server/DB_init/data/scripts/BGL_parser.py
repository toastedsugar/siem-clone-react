# Parse IBM BlueGene data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "Timestamp",
        "Year",
        "Month",
        "Day",
        "Node",
        "Time",
        "Type",
        "Component",
        "Level",
        "Content"
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/BGL/BGL_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line.split(" ", 9)      # Removing first two characters in data
        del(splitline[0])       # Remove label index
        del(splitline[4])       # Remove NodeRepeat index (redundant data)

        # Split full date into year, month and day
        date = splitline[1].split(".", 2)
        splitline[1] = date[0]                  # Add year
        splitline.insert(2, date[1])            # Add month
        splitline.insert(3, date[2])            # Add day

        # print(splitline)
        exportData.append([counter] + splitline)

        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/BGL-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
