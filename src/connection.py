from pymongo import MongoClient

class Connection:


    def __init__(self, url, port, bd):
        self.client = MongoClient(url, port)
        self.db= self.client[bd]

    def getDB(self):
        return self.db

    def close(self):
        self.client.close();

