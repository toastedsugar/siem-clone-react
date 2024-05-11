Docker files provided by https://python.plainenglish.io/creating-a-simple-task-crud-app-with-fastapi-postgresql-sqlalchemy-and-docker-a2cb562a7dcf



The purpose of this module is to insert raw data from multiple raw log data files into an SQL database where it can be both analyzed by other python scripts or consumed by the fontend application. 

A production SIEM would constantly be getting live log data from devices and be analyzing it for any vulnerabilities. As I don't have access to live log data, or have the capacity to do analysis on that scale, I instead decieded to simulate it by using open source log data I found online. 

Data cleaning: 
Since I am using raw log data, the data must be cleaned in a way that makes it usable.




