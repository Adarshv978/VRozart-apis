from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .Envirment import get_environment_variables

env = get_environment_variables()
database_name= env.DATABASE_NAME
dialect = env.DATABASE_DIALECT
username = env.DATABASE_USERNAME
password = env.DATABASE_PASSWORD


def get_db_connection():
    
    # uri = f"mongodb+srv://{username}:{password}@cluster0.btwxxld.mongodb.net/?retryWrites=true&w=majority"
    # uri = "mongodb+srv://adarshjschamps:Ldfvc42TptAr7vAA@cluster0.btwxxld.mongodb.net/?retryWrites=true&w=majority"
    uri = "mongodb+srv://adarshv978:8qLLZ0mfYmgOszqB@cluster0.1vmvbwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Specify the server API version
    server_api = ServerApi('1')

    client = MongoClient(uri, server_api=server_api)
    try:
        # Access the specified database using the provided database name
        database = env.DATABASE_NAME
        print("Database name",database)
        db = client[database]
        print("Pinged your deployment. You successfully connected to MongoDB! Adarsh")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return None

