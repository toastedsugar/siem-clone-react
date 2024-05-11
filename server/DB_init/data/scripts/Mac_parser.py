# Parse Tunderbird data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "Month",
        "Day",
        "Time",
        "User",
        "Component",
        "PID",
        "Content"
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/Mac/Mac_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line.split(" ", 6)      # Removing first two characters in data
        del(splitline[1])

        component = splitline[4].partition("[")
        splitline[4] = component[0]
        splitline.insert(5, component[2][:-2])
        
        print(splitline)
        
        exportData.append(
            [counter] + splitline
        )  # Add the index to data and add it to master list
        
        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/mac-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
