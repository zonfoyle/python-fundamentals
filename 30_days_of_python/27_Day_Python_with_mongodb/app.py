import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId

load_dotenv()  # loads variables from .env

MONGODB_URI = os.getenv("MONGODB_URI")

client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]
students = db["students"]

print("✅ Connected! Databases:", client.list_database_names())

# ---------------------------
# INSERT (Create)
# ---------------------------
students.insert_one({
    "name": "Zonique",
    "country": "USA",
    "city": "San Francisco",
    "age": 28
})

students.insert_many([
    {"name": "David", "country": "UK", "city": "London", "age": 34},
    {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
    {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
])

print("✅ Inserted sample students.")

# ---------------------------
# FIND (Read)
# ---------------------------
one_student = students.find_one()
print("\n✅ One student (find_one):")
print(one_student)

print("\n✅ Students in Finland:")
for s in students.find({"country": "Finland"}, {"_id": 0, "name": 1, "city": 1}):
    print(s)

print("\n✅ Students age > 30 (sorted by age desc, limit 2):")
for s in students.find({"age": {"$gt": 30}}).sort("age", -1).limit(2):
    print(s)

# ---------------------------
# UPDATE
# ---------------------------
students.update_one(
    {"name": "Zonique"},
    {"$set": {"city": "New York"}}
)
print("\n✅ Updated Zonique's city to New York")

# ---------------------------
# DELETE
# ---------------------------
students.delete_one({"name": "John"})
print("\n✅ Deleted one student named John")

print("\n✅ Final students list:")
for s in students.find({}, {"_id": 0, "name": 1, "country": 1, "city": 1, "age": 1}):
    print(s)
