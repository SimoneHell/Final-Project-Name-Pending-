"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Meal, Food
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def create_new_user():
    user_data = request.get_json("User")
    user = User.signup(password=user_data["password"], email=user_data["email"], username=user_data["username"])
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

@api.route('/logout', methods=['DELETE'])
def user_logout():
    session.pop("email", None)
    if user is None:
        return jsonify({"msg": " Succesfully Logged out "})
    return redirect(url_for("login")) 


#-------------------------- MEALS -----------------------


@api.route('/meal', methods=['GET'])
def meal_list(): 
    meal = Meal.query.all()
    response_body_meal = list(map(lambda s: s.serialize(), meal))
    return jsonify(response_body_meal), 200

@api.route('/meal/<int:id>/information', methods=['GET'])
def get_meal_by_id(id):
    
    meal = Meal.get_meal_by_id(id)
    
    return(jsonify(meal.serialize()))


#--------------------- FOOD-----------------


@api.route('/food', methods=['GET'])
def food_list(): 
    food = Food.query.all()
    response_body_food = list(map(lambda s: s.serialize(), food))
    return jsonify(response_body_food), 200

@api.route('/food/<int:id>/information', methods=['GET'])
def get_food_by_id(id):
    
    food = Food.get_food_by_id(id)
    
    return(jsonify(food.serialize()))

# ----------------  FAVORITES -------------

@api.route('/user', methods=['GET'])
def getUser():
    user = User.query.all()
    response_body_user = list(map(lambda s: s.serialize(), user))
    return jsonify(response_body_user), 200    


