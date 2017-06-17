from pymongo import MongoClient
import os

db_uri = "localhost:27017"
username = ''
password = ''
database = 'climb'
if os.environ['PYTHON_ENV'] != 'development':
    username = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']
    if os.environ['PYTHON_ENV'] == 'testing':
        db_uri = 'mongodb://' + username + ':' + password + '@ds129442.mlab.com:29442/climb-testing'
        database = 'climb-testing'
    elif os.environ['PYTHON_ENV'] == 'production':
        db_uri = 'mongodb://' + username + ':' + password + '@cluster0-shard-00-00-tdqdr.mongodb.net:27017,cluster0-shard-00-01-tdqdr.mongodb.net:27017,cluster0-shard-00-02-tdqdr.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

client = MongoClient(db_uri)

def db (collection):
    return client[database][collection]
