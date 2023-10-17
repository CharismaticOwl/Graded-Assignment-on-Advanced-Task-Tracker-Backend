from flask import Flask

app = Flask(__name__)

@app.route('/register', methdods = ['POST'])
def user_registration():

    return "work in progress. (User registration page)"

@app.route('/login', methods=['POST'])
def user_login():

    return "work in progress. (User login page)"

@app.route('/tasks', methods=['POST'])
def task_creation():

    return "work in progress. (Task creation page)"

@app.route('/tasks', methods=['GET'])
def task_retrieval():

    return "work in progress. (Task retrieval page)"

@app.route('/tasks/<task_id>', methods=['PUT'])
def task_update():

    return "work in progress. (Task Updation page)"

@app.route('/tasks/<task_id>', methods=['DELETE'])
def task_deletion():

    return "work in progress. (Task Deletion page)"

if __name__ == '__main__':
    app.run(debug=True, port=3000)