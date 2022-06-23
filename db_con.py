#from configparser import ConfigParser
#from run import 
#from run import app
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#app=Flask(__name__)


#file="config.ini"
#config=ConfigParser()
#config.read(file)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/student'
#v=app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+config['mysql']['user']+":"+config['mysql']['pswd']+"@"+config['mysql']['host']+"/"+config['mysql']['dbase']
#print(": : ",v)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/student'
db=SQLAlchemy()
#db.init_app(app)