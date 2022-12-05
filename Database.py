import os
from pymongo import *
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()

login = os.getenv("LOGIN")
uri_env = os.getenv("URI")
user = os.getenv("USER")

uri = "mongodb://" + str(user) + ":" + str(login) + "@" + str(uri_env)


def authenticate():
    try:
        app.mongodb_client = MongoClient(uri)
        app.database = app.mongodb_client['stickers']
    except Exception as e:
        print("Could not connect to database!\nException in Database.py:\n\n" + str(e))
    else:
        print("Connected to the database!")


authenticate()
