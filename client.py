from pymongo import MongoClient
import json


def establishConnection():
    file = open('connectionreq.json', 'rb')
    data = json.load(file)
    # data = json.loads('connectionreq.json')
    lhost = data['connectionreqs']['host']
    lport = data['connectionreqs']['port']
    client = MongoClient(lhost, int(lport))
    return client
