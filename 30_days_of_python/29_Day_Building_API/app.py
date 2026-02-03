from flask import Flask, jsonify, request
import pymongo
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["thirty_days_of_python"]

@app.route("/api/students", methods=["GET"])
def get_students():
    students = list(db.students.find({}, {"_id": 0}))
    return jsonify(students)

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json
    db.students.insert_one(data)
    return jsonify({"message": "Student added"}), 201

if __name__ == "__main__":
    app.run(debug=True)
