from flask import Flask, json, render_template, request
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import auth
from auth import *
import os

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
import sqlite3
import mimetypes

mimetypes.add_type('application/javascript', '.js')
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
app.config.from_object(__name__)
app.register_blueprint(auth.bp)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route("/", methods=['GET'])
def root():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('./index.html', users=users)


@app.route("/play", methods=['GET', 'POST'])
def play(name=None):
    if request.method == "GET":
        return render_template('./play.html', name=name)

    if request.method == "POST":
        pass

@app.route("/practice", methods=['GET', 'POST'])
def practice(name=None):
    if request.method == "GET":
        return render_template('./practice.html', name=name)

@app.route("/leaderboard", methods=['GET'])
def scores():
    if request.method == "GET":
        conn = get_db_connection()
        leaders = conn.execute('SELECT u.username, r.prompt_title, r.wpm, r.mistakes FROM races r INNER JOIN users u ON r.user_id = u.user_id').fetchall()

        conn.commit()
        return render_template('./leaderboard.html', leaders=leaders)

@app.route("/save", methods=['POST'])
def save():
    if request.method == "POST":
        res = request.json
        prompt_id = res['prompt_id']
        prompt_title = res['prompt_title']
        wpm = res['wpm']
        mistakes = res['mistakes']
        user_id = get_user_id()
        conn = get_db_connection()
        races = conn.execute("INSERT INTO races (prompt_id, prompt_title, wpm, mistakes, user_id) VALUES (? , ?, ?, ?, ?)",
                             (prompt_id, prompt_title, wpm, mistakes, user_id))
        conn.commit()

        return res


# Listener

if __name__ == "__main__":

    # Port
    app.run(port=3000, debug=True)