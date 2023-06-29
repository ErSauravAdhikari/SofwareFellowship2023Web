from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# Turning the debug mode will restart the server automatically in case of changes to the code
app.run(debug=True)