from pymongo import MongoClient

def db (collection):
    client = MongoClient('mongodb://brandonprice:climb3131harvard@cluster0-shard-00-00-tdqdr.mongodb.net:27017,cluster0-shard-00-01-tdqdr.mongodb.net:27017,cluster0-shard-00-02-tdqdr.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
    return client['climb'][collection]
