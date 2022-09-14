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
    response_body = "Hello, world!"
    return jsonify(response_body), 200


@api.route('/user', methods=['GET'])
def show_users():
    users = User.query.all()
    all_users_ll = []
    for user in users:
        all_users_ll.append({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            
            })
    return jsonify(all_users_ll), 200

@api.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    try:
        user_final = ({
            'id':user.id,
            'username':user.username,
            'email':user.email,
            
            })
        return jsonify(user_final), 200
    except Exception as error:
        return jsonify("Este usuario no existe")
        
   

@api.route('/signup', methods=['POST'])
def create_new_user():
    user_email = request.json.get('user-email', None)
    user_password = request.json.get('user-password', None)
    user_username = request.json.get('user-name', None)
    user = User.signup(password=user_password, email=user_email, username=user_username)
    db.session.add(user)
    db.session.commit()

    if user is not None:
        print(user)
        return jsonify({"message":"User created succesfully!"}), 201
    else:
        return jsonify({"message":"Something went wrong, Try again!"}), 500


@api.route('/login', methods=['POST'])
def user_login():
    email = request.json.get('user-email', None)
    password = request.json.get('user-password', None)
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

@api.route('/user/favorites', methods=['GET'])
def getUserFavorites():
    favorites = Favorites.query.all()
    response_body = list(map(lambda s: s.serialize(), favorites))
    return jsonify(response_body)

    # ---- Add Favorite Meal and Food -----

@api.route('/user/favorites/meal/<int:meal_id>', methods=['POST'])
def meals_fav():
    meals_fav = Favorites()
    meals_fav.user_id = request.json.get("user_id", None)
    meals_fav.meal_id = request.json.get("meal_id", None)
    db.session.add(meal_fav)
    db.session.commit()
    return jsonify["msg":"Everything went Ok"], 200


@api.route('/user/favorites/food/<int:food_id>', methods=['POST'])
def foods_fav():
    foods_fav = Favorites()
    foods_fav.user_id = request.json.get("user_id", None)
    foods_fav.food_id = request.json.get("food_id", None)
    db.session.add(food_fav)
    db.session.commit()
    return jsonify["msg":"Everything went Ok"], 200


    # -------- Delete Favorite Meal and Food --------- 

    
@api.route('/user/favorites/meal/<int:meal_id>', methods=['DELETE'])
def deletePlanetsFav(meal_id):
    delete_fav_meal = Favorites.query.get("meal")
    if delete_fav_meal is None: 
        raise APIException('User was not found', status_code=404)
    db.session.delete(delete_fav_meal)
    db.session.commit()
    return jsonify("Succesfully Deleted"), 200 

@api.route('/user/favorites/food/<int:food_id>', methods=['DELETE'])
def deleteFoodFav (food_id ):
    delete_fav_food = Favorites.query.get("food")
    if delete_fav_food is None: 
        raise APIException('User was not found', status_code=404)
    db.session.delete(delete_fav_food)
    db.session.commit()
    return jsonify("Succesfully Deleted"), 200 