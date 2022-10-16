from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == '__main__':
    mongodbclient = MongoDBClient()
    print("Collection name: ", mongodbclient.database.list_collection_names())