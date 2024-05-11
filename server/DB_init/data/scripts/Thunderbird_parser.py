# Parse Tunderbird data

import os
import re
import csv

# The first row is the CSV header
exportData = [
    [
        "LineId",
        "Timestamp",
        "Date",
        "User",
        "Month",
        "Day",
        "Time",
        "Location",
        "Component",
        "PID",
        "Content",
    ]
]

# os.path.dirname(__file__) allows for module relative paths to be used
CURRENT_DIR = os.path.dirname(__file__)

# With guarantees that the file is automatically closed when the script finishes execution
with open(
    CURRENT_DIR + "/../loghub-data-raw/Thunderbird/Thunderbird_2k.log", mode="r"
) as input:
    counter = 1

    # Read data line by line
    for line in input:
        # Clean up the data
        splitline = line[2:].split(" ", 8)      # Removing first two characters in data
        splitline[6] = splitline[6][:-1]        # Remove the trailing ':' in splitline[6]
        
        # Extract the PID from the splitline[7] and insert it into the list at splitline[8]
        try:
            pid = re.search(r'\[.*?\]', splitline[7]).group(0).strip("[]")
            splitline.insert(8, pid)
        except:
            splitline.insert(8, 0)

        splitline[7] = splitline[7].partition("[")[0]
        
        exportData.append(
            [counter] + splitline
        )  # Add the index to data and add it to master list

        counter += 1

# print(exportData)

# Export data into a CSV file
with open(CURRENT_DIR + "/../cleaned-data/thunderbird-clean.csv", "w") as csvfile:
    writer = csv.writer(csvfile, dialect="excel", delimiter="|")
    writer.writerows(exportData)
