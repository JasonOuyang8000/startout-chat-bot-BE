import models
from dotenv import load_dotenv
import os
from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
load_dotenv()


#Connects to DATABASE from Database URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

models.db.init_app(app)


def root():
    return 'ok'
app.route('/', methods=["GET"])(root)

@app.route('/investor-portal/',methods=['GET'])
def investor():
    try:
        print('link to become an investor')
        return{'link':'https://startout.org/investor-portal/','message':'Can I help you with anything else?'}
    except print("investor's link is not active"):
        return{'message':"investor's link is not active"},404


@app.route('/founder-programs/',methods=['GET'])
def founder():
    try:
        print('Getting support as a founder?')
        return{'link':'https://startout.org/founder-programs/','message':'Can I help you with anything else?'}
    except print("founder's link is not active"):
        return{'message':"founder's link is not active"},404

@app.route('/mentors/',methods=['GET'])
def mentor():
    try:
        print('Being a mentor')
        return{'link':'https://startout.org/mentors/','message':'Can I help you with anything else?'}
    except print("mentor's link is not active"):
        return{'message':"mentor's link is not active"},404


@app.route('/donate/',methods=['GET'])
def donate():
    try:
        print('looking to support through financial contributions')
        return{'link':'https://startout.org/donate/','message':'Can I help you with anything else?'}
    except print("donate's link is not active"):
        return{'message':"donate's link is not active"},404

@app.route('/the-networq/',methods=['GET'])
def networQ():
    try:
        print('I work for a local organization that supports founders, entrepreneurs, or professionals')
        return{'link':'https://startout.org/the-networq/','message':'Can I help you with anything else?'}
    except print("networQ's link is not active"):
        return{'message':"networQ's link is not active"},404


@app.route('/contact/',methods=['GET'])
def volunteering():
    try:
        print('I am a supporter looking to give back through volunteering.')
        return{'link':'https://startout.org/contact/','message':'Can I help you with anything else?'}
    except print("contact's link is not active"):
        return{'message':"contact's link is not active"},404

@app.route('/all-events/',methods=['GET'])
def start_out():
    try:
        print('I am looking for a local StartOut community')
        return{'link':'https://startout.org/all-events/','message':'Can I help you with anything else?'}
    except print("start_out's link is not active"):
        return{'message':"start_out's link is not active"},404


@app.route('/the-forum/',methods=['GET'])
def aspiring():
    try:
        print('I am an aspiring founder looking for inspiration.')
        return{'link':'https://startout.org/the-forum/','message':'Can I help you with anything else?'}
    except print("aspiring's link is not active"):
        return{'message':"aspiring's link is not active"},404

@app.route('/contact/',methods=['GET'])
def others():
    try:
        print("I don't seem to fit into any of these categories")
        return{'link':'https://startout.org/contact/','message':'Can I help you with anything else?'}
    except print("contact's link is not active"):
        return{'message':"contact's link is not active"},404

@app.route('/user_input',methods=['POST'])
def user_input():
    try:
        input = request.json['input']
        print("user input has been recieved")
        return{'input'}
    except print("contact's link is not active"):
        return{'message':"contact's link is not active"},404


# Runs Flask Server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
