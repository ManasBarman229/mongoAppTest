from pymongo import MongoClient
# import urllib.parse
from flask import Flask, request, render_template
# from flask_pymongo import PyMongo


# define the flask app
app = Flask(__name__)


# # define the mongodb client
# client = MongoClient(port=27017)

client = MongoClient(
    "mongodb+srv://Manas_database:%40qwerty%40123@dataset.xni2nb8.mongodb.net/test")
db = client.projectData

# # define the database to use
# db = client.student_data


# mongodb atlas config

# username = urllib.parse.quote_plus('Manas_database')
# password = urllib.parse.quote_plus("@qwerty@123@")
# app.config["SECRET_KEY"] = "d10b6b145a28543bd613eecd0d4e6fdec14a8cc5"
# app.config["MONGO_URI"] = "mongodb+srv://{}:{}@cluster0.fzqzl4h.mongodb.net /?retryWrites = true & w = majority".format(
#     username, password)

# # setup mongodb
# mongodb_client = PyMongo(app)
# db = mongodb_client.db


# define the home page route
@app.route('/')
def home():
    return render_template("index.html")


# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Language'] = request.form['Language']
        data['Original_Text'] = request.form['Original']
        data['Transliterated_Text'] = request.form['Transliterated']
        data['Sentiment'] = request.form['Sentiment']

        db.projectData.insert_one(data)

    return render_template("index.html")


# start the flask server
if __name__ == '__main__':

    app.run(debug=True)
