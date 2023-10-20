from flask import Flask, request
import hashlib
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.task_tracker

@app.route('/hello', methods = ['GET'])
def hello():
    return "Hello World!"

@app.route('/register', methods =['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')

    password = request.form.get('password')

    password = hashlib.sha256(password.encode()).hexdigest()

    x = db.user.find_one({
        "name": name,
        "email": email
    })

    if (x):
        return "User already registered!"
    else:
        db.user.insert_one({
            "name":name,
            "email": email,
            "password": password
        })

        return "User has been successfully registered"
    

# @app.route('/login', methods=['POST'])
# def user_login():

#     return "work in progress. (User login page)"

# @app.route('/tasks', methods=['POST'])
# def task_creation():

#     return "work in progress. (Task creation page)"

# @app.route('/tasks', methods=['GET'])
# def task_retrieval():

#     return "work in progress. (Task retrieval page)"

# @app.route('/tasks/<task_id>', methods=['PUT'])
# def task_update():

#     return "work in progress. (Task Updation page)"

# @app.route('/tasks/<task_id>', methods=['DELETE'])
# def task_deletion():

#     return "work in progress. (Task Deletion page)"

if __name__ == '__main__':
    app.run(debug=True, port=3000)