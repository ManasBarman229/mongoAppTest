from pymongo import MongoClient
from flask import Flask, request, render_template


# define the flask app
app = Flask(__name__)


# define the mongodb client

client = MongoClient(
    "mongodb+srv://Manas_database:%40qwerty%40123@dataset.xni2nb8.mongodb.net/test")
# define the database to use
db = client.projectData


# define the home page route
@app.route('/')
def home():
    return render_template("index.html")


# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Original_language'] = request.form['Original_language']
        data['Original_Text'] = request.form['Original_text']
        data['Transliterate_language_1'] = request.form['Transliterate_language_1']
        data['Transliterated_text_1'] = request.form['Transliterated_text_1']
        data['Transliterate_language_2'] = request.form['Transliterate_language_2']
        data['Transliterated_text_2'] = request.form['Transliterated_text_2']
        data['Sentiment'] = request.form['Sentiment']

        db.projectData.insert_one(data)

    return render_template("index.html")


# start the flask server
if __name__ == '__main__':

    app.run(debug=True)
