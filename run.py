from flask import Flask
from flask_restful import Resource, Api
from db_con import db
#from resources.user import Users, Home
from resources.user import *

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akashmukherjee@localhost/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

api = Api(app)
#api.add_resource(Users, '/')
api.add_resource(Home, '/')
api.add_resource(Users, '/create')
api.add_resource(Insert, '/insert')
api.add_resource(Fetch, '/fetch')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')

if __name__== "__main__":
    
    app.run(debug=True, host="0.0.0.0", port="5001", use_reloader=True)
    #print(app)
