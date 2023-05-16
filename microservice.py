from flask import Flask, request, json

app = Flask(__name__)


class Contacts:

    def __init__(self):
        self.user_credentials = {
            "user1": 'password1',
            "user2": 'password2'
        }

    def get_users(self):
        return self.user_credentials

    def set_user(self, username, password):
        self.user_credentials[username] = password

    def get_password(self, username):
        return self.user_credentials[username]

    def change_password(self, username, password):
        self.user_credentials[username] = password

    def delete_user(self, username):
        self.user_credentials.pop(username)

def check_credentials(login):
    if login['username'] in users.get_users().keys():
        if users.get_users().get(login['username']) == login['password']:
            return True
        else:
            return False
    else:
        return False

@app.route("/", methods=['GET'])
def hello():
    return "<p>Hello</p>"

@app.route("/validate", methods=['GET', 'POST'])
def user_validation():
    if request.method == 'POST':
        login = {"username": request.form['username'],
                 "password": request.form['password']
                  }
        res = check_credentials(login)
        return app.response_class(json.dumps(res), content_type='application/json')

@app.route("/users", methods=['GET', 'POST', 'PUT', 'DELETE'])
def contacts():
    if request.method == 'GET':
        return app.response_class(json.dumps(users.get_users()), content_type='application/json')

    # Update
    elif request.method == 'POST':
        login = {"username": request.form['username'],
                 "password": request.form['password']
                 }

        users.change_password(login['username'], login['password'])

        return app.response_class(json.dumps('Updated user.'), content_type='application/json')

    # Create
    elif request.method == 'PUT':
        login = {"username": request.form['username'],
                 "password": request.form['password']
                 }
        print(login)
        users.set_user(login['username'], login['password'])

        return app.response_class(json.dumps('Created user.'), content_type='application/json')

    # Delete
    elif request.method == 'DELETE':
        login = {"username": request.form['username']
                 }
        users.delete_user(login['username'])
        return app.response_class(json.dumps('Deleted user.'), content_type='application/json')

users = Contacts()