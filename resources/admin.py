from flask_restful import Resource
from flask import request, jsonify, make_response
from models import db_admin, db_user

class Admin(Resource):
    def post(self):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            u_id=data['uid']
            print(u_id)
            try:
                person=db_user.User.query.filter_by(id=u_id).first()
                u_name=person.username
                u_mail=person.email
                print("===",u_name)
                admin=db_admin.Admin(uid=u_id, adminName=u_name, email=u_mail)
                #print(user)
                db_admin.db.session.add(admin)
                db_admin.db.session.commit()         
                return "admin data successfully inserted"
            except Exception as e:
                print("error",e)
                return make_response('Check Again')

    def get(self):
        val=[]
        #value={}
        adms=db_admin.Admin.query.all()
        for ad in adms:
            dic={}
            aid=ad.aid
            uid=ad.uid
            name=ad.adminName
            mail=ad.email
            #print(id," ",name," ",mail)
            dic=aid,uid,name,mail
            #print("ss",dic)
            val.append(dic)
            print("\n")
            #print(val)
        return jsonify(val)


            
