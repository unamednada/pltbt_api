from pymongo import MongoClient


DB_URI = "mongodb+srv://admin:admin1@cluster0.8om9x.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(DB_URI)
