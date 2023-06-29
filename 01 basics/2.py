from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return_string = """
            <h1> Learning Path and Query Params!</h1><br/>
            <a href="/users/abc">Path</a> and <br/>
            <a href="/search?q=abc">Query Parameters</a>
           """
    return return_string

@app.route('/users/<username>')
def get_user(username):
    return f'User profile: {username}'

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Searching for: {query}'

app.run(debug=True)