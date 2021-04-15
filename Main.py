# Import this to connect with Dialogflow
from flask import Flask, request, make_response, jsonify

# Importing my python functions
from AnswerMaker import *


# Defining answer generation function
def createAnswer(intent):
    out = intentQueryMatcher(intent)
    return out


# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/')
def index():
    return 'Hello World!'


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # fetch intent from json
    intent = req.get('queryResult').get('intent').get('displayName')

    # return a fulfillment response
    out = createAnswer(intent)
    return {'fulfillmentText': out}


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app
if __name__ == '__main__':
    app.run()