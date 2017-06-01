from pymongo import MongoClient
import os

def db (collection):

    db_uri = 'mongodb://brandonprice:climb3131harvard@cluster0-shard-00-00-tdqdr.mongodb.net:27017,cluster0-shard-00-01-tdqdr.mongodb.net:27017,cluster0-shard-00-02-tdqdr.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
    if os.environ['PYTHON_ENV'] == 'development':
        db_uri = "localhost:27017"

    client = MongoClient(db_uri)
    return client['climb'][collection]
