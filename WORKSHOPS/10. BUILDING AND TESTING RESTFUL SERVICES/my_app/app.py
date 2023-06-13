from flask import Flask, render_template, request, redirect, g
import sqlite3
import os

main_app = Flask(__name__)

@main_app.route('/')
def index():
    return redirect('/register')


# Register page allows user to add username and sport
@main_app.route("/register")
def register():
    my_games = ["Poker", "Battleship", "Chess", "Pick-up Sticks"]
    return render_template('register.html', games=my_games)


# Function to get current database
def get_db():
    db_name = 'webappdb.db'
    # Get path to database
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, db_name)
    # defining g module's database attribute 
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path)
    return db


# Teardown function allows databse to be closed after request.
@main_app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        

# Executes database queries and returns the results
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    result = cur.fetchall()
    cur.close()
    get_db().commit()
    return (result[0] if result else None) if one else result
    

# Submit checks if username is already in database and return corresponding page.
@main_app.route('/submit', methods=["POST"])
def submit():
    username = request.form.get('name')
    game = request.form.get('game')
    with main_app.app_context():
        try:
            query_db("INSERT INTO Users(username, game) VALUES(?,?)", (username, game))
            return render_template('register_success.html', username=username)
        except:
            return render_template('register_fail.html')
        

@main_app.route('/users', methods=["POST", "GET"])
def users():
    result = query_db("SELECT username, game FROM Users")
    if request.method == "POST":
        output = []
        output.append("User : Game")
        for user in result:
            output.append(f"{user[0]}: {user[1]}")
        return render_template('users.html', users=output)
    elif request.method == "GET":
        output = {}
        for i, user in enumerate(result):
            output[i] = [user[0], user[1]]
        return output
    