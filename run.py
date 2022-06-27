from flask import Flask
from flask_restful import Resource, Api
from db_con import db
#from resources.user import Users, Home
from resources.user import *
from resources.admin import *

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akashmukherjee@localhost/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

api = Api(app)
api.add_resource(User, '/')
api.add_resource(Login, '/login')
api.add_resource(Authentication, '/auth')
api.add_resource(Admin, '/admin')


if __name__== "__main__":
    
    app.run(debug=True, host="0.0.0.0", port="5001", use_reloader=True)
    #print(app)
