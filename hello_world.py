# hello_world.py

from flask import Flask
app = Flask(__name__) #the _name_ argument indicates the app's module or package

@app.route('/')#decorator, tells Flask which path to display the result of the function
def hello_world():
    return 'Hello World!'