import sys
import time
from Csvfile import importFile
from client import establishConnection


def main(argv):
    print ''
    reader = importFile(argv[0])
    # at this point, all the data is in dictionary format

    client = establishConnection()

    if argv[1] in client.database_names():  # verfify if the database already exists
        print 'The indicated database already exists'

    db = client[argv[1]]  # creation of the collection

    if argv[2] in db.collection_names():
        print 'The indicated collection already exists, let me clean it'
        db[argv[2]].drop()  # making sure the collection mycollection is clean

    print 'I will proceed to create the collection as you wanted it'
    collection = db[argv[2]]  # creating the collection mycollection

    print '========================================================'
    print ''
    print 'Importing all the csv entries in the database'



    toolbar_width = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(0.1) # do real work here
        for item in reader:
            collection.insert_one(item)
    # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("\n")
        #  at this point the database is built with the csv data

    collectioninfo = db.command("collStats", "mycollection")
    print 'I created the database: ', argv[1]
    print 'Inside that database I created the collection: ', argv[2]
    print 'All the documents have the following fields: ', reader.fieldnames
    print collectioninfo["count"], "documents were created"
    print collectioninfo["size"], "is the size of the collection"

if __name__ == "__main__":
    main(sys.argv[1:])
