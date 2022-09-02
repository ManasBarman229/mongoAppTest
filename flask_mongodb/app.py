from flask import Flask, request, render_template
from pymongo import MongoClient

# define the mongodb client
client = MongoClient(port=27017)

# define the database to use
db = client.student_data

# define the flask app
app = Flask(__name__)

# define the home page route


@app.route('/')
def home():
    return render_template("index.html")
