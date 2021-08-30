# import dependencies
from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# create our first route, or root
@app.route('/')
def hello_world():
    return 'Hello world'


