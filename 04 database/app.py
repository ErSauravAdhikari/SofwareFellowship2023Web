from flask import Flask, redirect, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URL = "################################################################"

client = MongoClient(MONGODB_URL)

db = client['default']
collection = db['contact_us']



@app.route('/')
def list_values():
    return render_template('list.html', values=collection.find())


@app.route('/form', methods=['GET'])
def render_form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'message': request.form['message']
    }
    collection.insert_one(data)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
