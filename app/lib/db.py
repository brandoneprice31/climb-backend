from pymongo import MongoClient

def db (collection):
    client = MongoClient()
    return client['climb'][collection]
