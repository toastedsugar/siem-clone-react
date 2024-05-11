# Parse Android data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "Month",
        "Day"
        "Time",
        "PID",
        "TID",
        "Level",
        "Component",
        "Content"
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/Android/Android_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line.split(" ", 8)      # Removing first two characters in data
        if splitline[2] == '': del splitline[2]        # delete empty indexes if they're empty
        if splitline[3] == '': del splitline[3]        # delete empty indexes if they're empty
        
        # Spliting the date index into month and day
        date = splitline[0].partition("-")
        splitline[0] = date[0]
        splitline.insert(1, date[2])

        #splitline[5] = splitline[5][:-1]        # Remove the trailing ':' in splitline[6]
        #splitline[5] = splitline[5].rstrip()
    
        print(counter, "\t", splitline)
        splitline[5] = splitline[5][:-1]        # Remove trailing character

        exportData.append(
            [counter] + splitline
        )  # Add the index to data and add it to master list

        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/android-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
