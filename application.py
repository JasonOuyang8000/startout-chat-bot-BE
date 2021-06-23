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


@app.route('/userportal', methods=['POST'])
def user_portal():
    try:

     
        response = {"investor":['investor','banker','lender','shareholder','stockholder','venture capitalist','backer',"capitalist",'stakeholder','angel investor','Becoming and investor'],'founder':['founder','creator',"author",'establisher','architect','developer','builder','Getting support as a founder'], 'mentor':['Being a mentor','teacher',"guide",'tutor','instructor','advisor','supporter','coach','counsellor','mentor'],'donate':['donate','give','contribute','make a donation','give a donation','make a contribution','contribution','pledge','grant','hand out','gift','money'],'networQ':['network',"networQ",'connect','reach out', "community",'connection'],'options':['option',"other",'help',"contact","options",'others',"assist",'assistance'],'events':["events",'event','local','community','insparation','city']}
        user_input = request.json['input']
     
     
        print(user_input)
        if user_input in response["investor"]:
            return{'link':'https://startout.org/investor-portal/','message':'Can I help you with anything else?'}
        elif user_input in response['founder']:
            return{'link':'https://startout.org/founder-programs/','message':'Can I help you with anything else?'}
        elif user_input in response['mentor']:
            return{'link':'https://startout.org/mentors/','message':'Can I help you with anything else?'}
        elif user_input in response['donate']:
            return{'link':'https://startout.org/donate/','message':'Can I help you with anything else?'}
        elif user_input in response['networQ']:
             return{'link':'https://startout.org/the-networq/','message':'Can I help you with anything else?'}
        elif user_input in response['options']:
            return{'link':'https://startout.org/contact/','message':'Can I help you with anything else?'}
        elif user_input in response['events']:
            return{'link':'https://startout.org/all-events/','message':'Can I help you with anything else?'}
        else:
            return {'message': 'Sorry,I do not understand.'}
        
    except Exception as e:
        print(e)
        pass


# Runs Flask Server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
