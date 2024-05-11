from typing import Union

from fastapi import FastAPI
import psycopg2
import os
import json

app = FastAPI()


# Establish connection with database
def Open_DB():
    # Returns `default_value` if the key doesn't exist
    db_db = os.environ.get("POSTGRES_DB", "default_value")
    db_user = os.environ.get("POSTGRES_USER", "default_value")
    db_password = os.environ.get("POSTGRES_PASSWORD", "default_value")
    db_host = os.environ.get("POSTGRES_HOST", "127.0.0.1")
    db_port = os.environ.get("POSTGRES_PORT", "5432")

    print(type(db_db), type(db_user), type(db_password), type(db_host), type(db_port))
    """    """
    # Connect to the database
    conn = psycopg2.connect(
        database=db_db, user=db_user, password=db_password, host=db_host, port=db_port
    )

    return conn


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Insert firewall data into database
@app.post("/firewallData")
def InsertFirewallData():

    return {"Insert": "Firewall"}


# Retrieve all firewall data from database and send it to client
@app.get("/firewallData/all")
def GetFirewallData():
    conn = Open_DB()  # Establish connection
    cursor = conn.cursor()  # Create cursor
    cursor.execute("SELECT * FROM firewall_data")

    data = []

    # Format data as dictionary (javascript objects) 
    for line in cursor.fetchall():
        newdict = {
            "source_port": line[0],
            "destination_port": line[1],
            "nat_source_port": line[2],
            "nat_destination_port": line[3],
            "action": line[4],
            "bytes": line[5],
            "bytes_sent": line[6],
            "bytes_recieved": line[7],
            "packets": line[8],
            "elapsed_time": line[9],
            "packets_sent": line[10],
            "packets_recieved": line[11],
        }
        data.append(newdict)
    # print(data)
        
    conn.close()

    # json.dumps() is not necessary as fastapi will wrap everything in a json response object automatically
    return data
