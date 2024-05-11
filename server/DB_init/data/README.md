## About

Much of the open source data is provided in CSV format. However, some of the data has commas within the data itself, which causes errors when it's being parsed by postgres during the container initialzation procedure. This means that I need to parse the raw log data myself and export to CSV using a completely different delimeter.

The scripts directory contains the python scripts used to parse the raw log data into new CSV files using a '|' as the delimeter and exports the cleaned log data into the cleaned-data directory. 

If the provided CSV files have no issues with commas, there is no need to build a custom parser.


## Checklist:
 - Android          Not Clean       Cleaned
 - Apache           Clean           
 - BGL              Not Clean       Cleaned
 - Hadoop           Not Clean       Cleaned
 - HDFS             Clean
 - HealthApp        Not Clean       Skip
 - HPC              Clean
 - Linux            Clean                       Done
 - Mac              Not Clean       Cleaned
 - OpenSSH          Clean
 - OpenStack        Not Clean       Cleaned
 - Proxifier        Not Clean
 - Spark            Not Clean
 - Thunderbird      Not Clean       Cleaned     Done
 - Windows          Not Clean       
 - Zookeeper        Not Clean
