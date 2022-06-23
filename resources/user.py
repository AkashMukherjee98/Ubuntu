from flask_restful import Resource
from flask import request, jsonify
from models import db_user

class Home(Resource):
    def get(self):
        return "Welcome to Structure"

class Users(Resource):
    def get(self):
        #return "okk akash"
        db_user.db.create_all()
        return {'msg': 'Tables created'}

class Insert(Resource):
    def post(self):
        #return "okk"
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            user_name=data['username']
            print(user_name)
            user_email=data['email']
            print(user_email)
            # exit(0)
            user=db_user.User(username=user_name, email=user_email)
            print("---- :",user)
            db_user.db.session.add(user)
            db_user.db.session.commit()         
        return "insert data"


class Fetch(Resource):
    def get(self):
        #return "hi"
        val=[]
        #print("hello")
        users=db_user.User.query.all()
        for user in users:
            dic={}
            id=user.id
            name=user.username
            mail=user.email
            print(id," ",name," ",mail)
            dic=id,name,mail
            print("ss",dic)
            val.append(dic)
            print("\n")
            print(val)
        return jsonify(val)


class Update(Resource):
    def put(self):
        content_type = request.headers.get('Content-Type')
        if(content_type == 'application/json'):
            data = request.get_json()
            u_id=data['id']
            u_name=data['username']
            u_mail=data['email']
            print(u_id," ",u_name," ",u_mail)
            user = db_user.User.query.get(u_id)
            user.username = u_name
            user.email= u_mail
            db_user.db.session.commit() 
            return "update Sucessful"


class Delete(Resource):
    def delete(self):
        content_type = request.headers.get('Content-Type')
        if(content_type == 'application/json'):
            data = request.get_json()
            u_id=data['id']
            print(u_id)
            user=db_user.User.query.get(u_id)
            db_user.db.session.delete(user)
            db_user.db.session.commit()
            return "delete successful"

