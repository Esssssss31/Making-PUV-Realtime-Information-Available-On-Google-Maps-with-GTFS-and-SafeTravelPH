# here is an example code for utils.py that includes a function for reading data 
# from a MongoDB database.
# This function uses the pymongo library to connect to a MongoDB database 
# and read data from a specified collection. 
# The function takes the names of the database and collection as parameters, 
# and returns a list of dictionary objects containing the data from the collection.

from pymongo import MongoClient

def read_data_from_mongodb(database_name, collection_name):
    """
    Connects to a MongoDB database and reads data from a specified collection.
    :param database_name: Name of the database to connect to.
    :param collection_name: Name of the collection to read from.
    :return: List of dictionary objects containing the data from the collection.
    """
    client = MongoClient()
    database = client[database_name]
    collection = database[collection_name]
    data = list(collection.find())
    client.close()
    return data
