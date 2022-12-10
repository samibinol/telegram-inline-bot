import os
import sqlite3
import pymongo
from pymongo import *
from dotenv import load_dotenv
from fastapi import FastAPI

# app = FastAPI()

conn = sqlite3.connect('stickers.db')

c = conn.cursor()


# Basic database structure as of now:
# sid (string, representing the sticker id passed over by telegram)
# tags (list, the user-defined tags used to search the sticker)

def search(query):
    return None


def add(sid, tags):
    # Fetch row with matching SID and remove the sid to get the tags
    # Structure: "tag1,tag2,tag3"

    cursor = conn.execute("""SELECT * FROM stickers WHERE sid == ?""", (sid,))
    fa = cursor.fetchall()

    if len(fa) == 0:
        # Adding a new entry in the database
        c.execute("""INSERT INTO stickers VALUES (?, ?)""", (sid, tags))
        conn.commit()
        return 0
    else:
        # Removing the SID and adding the new tags
        fa2 = fa.pop(0)
        fa3 = fa2[:][1]
        result = fa3 + "," + tags
        # Updating the database
        c.execute("""UPDATE stickers SET tags = ? WHERE sid == ?""", (result, sid,))
        conn.commit()
        return 0


# Only uncomment to test the database connection:
# add("sduif67", "test54,test53,test98")
