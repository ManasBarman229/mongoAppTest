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


# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Name'] = request.form['name']
        data['Email'] = request.form['email']
        data['Age'] = request.form['age']
        data['DOB'] = request.form['dob']
        data['Department'] = request.form['department']
        data['Gender'] = request.form['gender']
        data['Address'] = request.form['address']
        data['Pincode'] = request.form['pincode']
        lang = []
        for i in "1234567":
            try:
                if request.form['language' + i] != "":
                    lang.append(request.form['language' + i])
            except Exception as e:
                pass
        data['Language'] = lang
        db.studentData.insert_one(data)

    return render_template("index.html")


# start the flask server
if __name__ == '__main__':

    app.run(debug=False)
