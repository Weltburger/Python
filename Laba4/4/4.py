import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652", "year": 2000},
  { "name": "Hannah", "address": "Mountain 21", "year": 2000},
  { "name": "Michael", "address": "Valley 345", "year": 2001},
  { "name": "Sandy", "address": "Ocean blvd 2", "year": 2015},
  { "name": "Betty", "address": "Green Grass 1", "year": 2010},
  { "name": "Richard", "address": "Sky st 331", "year": 2005},
  { "name": "Susan", "address": "One way 98", "year": 2007},
  { "name": "Vicky", "address": "Yellow Garden 2", "year": 2003},
  { "name": "Ben", "address": "Park Lane 38", "year": 2020},
  { "name": "William", "address": "Central st 954", "year": 2011},
  { "name": "Chuck", "address": "Main Road 989", "year": 1998},
  { "name": "Viola", "address": "Sideway 1633", "year": 1995}
]

# x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# x = mycol.find_one()
# print(x)

# for x in mycol.find():
#     print(x)
# Do not show id in output
# for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
#     print(x)

# for x in mycol.find({}, {"address": 0}):
#     print(x)


# myquery = {"address": "Park Lane 38"}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

# Find documents where the address starts with the letter "S" or higher
# myquery = {"address": {"$gt": "S"}}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)
#

# Find documents where the address starts with the letter "S"
# myquery = { "address": { "$regex": "^S" } }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

# Sort the result reverse alphabetically by name

# mydoc = mycol.find().sort("name", -1)
#
# for x in mydoc:
#     print(x)

# Change the address from "Valley 345" to "Canyon 123"
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
#
# mycol.update_one(myquery, newvalues)
#
# # print "customers" after the update:
# for x in mycol.find():
#     print(x)

# Update all documents where the address starts with the letter "S":
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
#
# x = mycol.update_many(myquery, newvalues)
#
# print(x.modified_count, "documents updated.")

# Limit the result to only return 5 documents
# myresult = mycol.find().limit(5)
#
# #print the result:
# for x in myresult:
#     print(x)

# myquery = {"year": {'$gt': 2010}}
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

# myquery = {"year": {'$gte': 2007, '$lt': 2015}}
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

# # Delete everything
# x = mycol.delete_many({})
