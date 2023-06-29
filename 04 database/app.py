from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URL = "################################"

client = MongoClient(MONGODB_URL)

db = client['default']
collection = db['contact_us']


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
    return 'Data saved successfully'

@app.route('/list')
def list_values():
    values = []
    for doc in collection.find():
        values.append(doc)
    return render_template('list.html', values=values)


if __name__ == '__main__':
    app.run()
