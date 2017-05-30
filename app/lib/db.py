from pymongo import MongoClient

def db (collection):
    client = MongoClient('mongodb://brandonprice:#climbdatabaseyoyo@ds157571.mlab.com:57571/heroku_d3d5n4vx')
    return client['climb'][collection]
