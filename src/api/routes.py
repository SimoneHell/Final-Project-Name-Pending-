"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = "Hello, world!"
    return jsonify(response_body), 200


@api.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    all_users_ll = []
    for user in users:
        all_users_ll.append({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'is_active':user.is_active,
            })
    return jsonify(all_users_ll), 200

@api.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    try:
        user_final = ({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'is_active':user.is_active,
            })
        return jsonify(user_final), 200
    except Exception as error:
        return jsonify("Este usuario no existe")
        
   

@api.route('/signup', methods=['POST'])
def create_new_user():
    user_data = request.get_json("User")
    user = User.signup(password=user_data["password"], email=user_data["email"])
    db.session.add(user)
    db.session.commit()

    if user is not None:
        print(user)
        return jsonify({"message":"User created succesfully!"}), 201
    else:
        return jsonify({"message":"Something went wrong, Try again!"}), 500


@api.route('/login', methods=['POST'])
def user_login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    print(request.json)
    user = User.query.filter_by(email=email, password=password).one_or_none()
    if user is None:
        return jsonify({"msg": "Something went wrong, please try again!"}), 401
    
    # token
    access_token = create_access_token(identity=user.email)
    return jsonify({ "token": access_token, "user_id": user.id, "email": user.email })