import pymongo

# Connect to local MongoDB
local_client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connect to MongoDB Atlas
atlas_client = pymongo.MongoClient("your_atlas_connection_string")

# Fetch data from local MongoDB
data = local_client["testdb"]["testcol"].find()

# Insert data into MongoDB Atlas
atlas_client["testdb"]["testcol"].insert_many(data)

print("Data migration to MongoDB Atlas completed.")