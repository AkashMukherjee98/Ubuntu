from flask_restful import Resource
from flask import request, jsonify, make_response
from models import db_user 
import jwt
from datetime import datetime,timedelta
import pytz
from dotenv import load_dotenv
load_dotenv('.env')
import os

class User(Resource):
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            user_name=data['username']
            user_email=data['email']
            print(user_email)
            user=db_user.User(username=user_name, email=user_email)
            db_user.db.session.add(user)
            db_user.db.session.commit()         
            return "insert data"

    def get(self):
        val=[]
        users=db_user.User.query.all()
        for user in users:
            dic={}
            id=user.id
            name=user.username
            mail=user.email
            dic=id,name,mail
            val.append(dic)
            print("\n")
            #print(val)
        return jsonify(val)

    def put(self):
        content_type = request.headers.get('Content-Type')
        if(content_type == 'application/json'):
            data = request.get_json()
            u_id=data['id']
            u_name=data['username']
            u_mail=data['email']
            user = db_user.User.query.get(u_id)
            user.username = u_name
            user.email= u_mail
            db_user.db.session.commit() 
            return "update Sucessful"

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

class Login(Resource):
    def post(self):
        try:
            auth = request.authorization
            try:
                #sql="select usersId,usersPassword from company.users where usersId={} and usersPassword={};".format(auth.username,"'"+auth.password+"'")
                record=db_user.User.query.filter_by(id=auth.username, username=auth.password).first()
                #print("record: ",record)
                if record:
                    SECRET_KEY=os.getenv("SCKY")
                    #print("seckey: ",SECRET_KEY)
                    u_id=record.id
                    u_mail=record.email
                    now=datetime.now() 
                    d_utc = now.astimezone(pytz.UTC)
                    delta=datetime.now()+timedelta(minutes=20)
                    dt_utc = delta.astimezone(pytz.UTC)
                    #print('Current time in UTC Time-zone: ', dt_utc)
                    json_data = {
                        "id": u_id,
                        "pass":u_mail,
                        "iat":d_utc,
                        "exp": dt_utc
                    }
                    #print(json_data["id"])
                    encode_data = jwt.encode(json_data, key=SECRET_KEY, algorithm="HS256")
                    return jsonify({'msg': encode_data})                    
                else:
                    return jsonify({"msg": "Check id and password carefully"})    
            except Exception as e:
                print("Error: ",e)
                return jsonify({"msg": "Check again"})
        except Exception as e:
            print("Error: ",e)
            return make_response("Error")


class Authentication(Resource):
    def get(self):
        headers = request.headers
        bearer = headers.get('Authorization')
        token_bearer = bearer.split()[1]
        #print("========",token_bearer)
        SECRET_KEY = os.getenv("SCKY")
        #print(":::::",SECRET_KEY)    
        decode_data = jwt.decode(token_bearer,SECRET_KEY,algorithms=['HS256'])
        #print("----",decode_data)
        try:
            if token_bearer:    
                decode_data = jwt.decode(token_bearer,SECRET_KEY,algorithms=['HS256'])
                first_value = list(decode_data.items())[0][1]
                now_time=list(decode_data.items())[2][1]
                dt_now_obj = datetime.fromtimestamp(now_time)
                dtt_utc = dt_now_obj.astimezone(pytz.UTC)
                ch_ti=dtt_utc+timedelta(seconds=30)
                if str(datetime.now().astimezone(pytz.UTC))>str(ch_ti):
                    return "Token Expired"  
                else:
                    try:                    
                        record=db_user.User.query.filter_by(id=first_value)
                        if record:
                            return jsonify({"msg": "Token is valid"},{"user": decode_data}) 
                    except Exception as e:
                        #print("Error: ",e)
                        return jsonify({"msg": "Invalid Token"})            
        except Exception as e:
            #print("Error: ",e)
            return jsonify({"msg": "Check Again"})