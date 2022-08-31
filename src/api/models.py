from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorites")
    
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    values = db.Column(db.String(120), unique=True, nullable=False)
    ingredients = db.Column(db.String(120), unique=True, nullable=False)
    # Calculator(?)   

    def __repr__(self):
        return f'<Meals {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name
            "values": self.values
        }

class Favorites(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    meals_id = db.Column(db.Integer, db.ForeignKey('meals.id'))
    user = db.relationship("User")
    meals = db.relationship("Meals")

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
       
        return {
            "id": self.id,
            "user_id":self.user_id,
            "meals_id":self.meals_id
        }

#class Calculator (db.Model):                         Dont know if necessary
   
#   id = db.Column(db.Integer, primary_key=True)
#def __repr__(self):
#       return { "id": self.id}
#def serialize(self): return {}