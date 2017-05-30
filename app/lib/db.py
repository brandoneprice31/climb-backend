from pymongo import MongoClient

def db (collection):
    client = MongoClient('mongodb://heroku_d3d5n4vx:dg9pkft99s9k4hp1v74qads3bs@ds157571.mlab.com:57571/heroku_d3d5n4vx')
    return client['climb'][collection]
