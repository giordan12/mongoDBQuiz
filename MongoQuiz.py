import pymongo
from Csvfile import importFile
from client import establishConnection
from pymongo import MongoClient

# One file to create the connections
# Another file to import the data from the csv file
# Another file that combines both of them into a single one

reader = importFile('TourneySeeds.csv')
# at this point, all the data is in dictionary format

client = establishConnection()
db = client.mydatabase  # creation of the collection
collection = db.mycollection
collection.remove()  # cleaning the collection
posts = db.posts

for item in reader:
    post_id = posts.insert_one(item).inserted_id
#  at this point the database is built with the csv data
