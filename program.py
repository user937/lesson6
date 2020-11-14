from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/kozintsev')
def kozintsev():
    return 'Hello from CI with GitHub Actions by kozintsev'
