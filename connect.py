
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def connectDB():
    uri = "mongodb+srv://efekoyuncu:eFe2012.@cluster0.s3vsylf.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# Usage example
db = connectDB()
if db:
    # Perform database operations
    pass




