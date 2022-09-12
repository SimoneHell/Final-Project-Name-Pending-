from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

# Relationships --> https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships

class User(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #favorites = db.relationship("Favorites")
    
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }

    @classmethod
    def signup(cls, email, password):
        instance = cls(
            username=username,
            email=email,
            password=password
        )
        if isinstance(instance, cls):
            return instance
        else:
            return None
    
    @classmethod
    def login(cls, email, password):
        user_data = cls.query.filter_by(
            email=email
        ).one_or_none()
        if (not isinstance(user_data, cls)):
            return user_data
        if user_data.password == password:
            return user_data
        else:
            return False



class Food(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    sumarize = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    nutrients = db.Column(db.String(80), unique=False, nullable=False)
    #favorites = db.relationship("Favorites")
    def __repr__(self):
        return f'<Ingredients {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "sumarize": self.sumarize,
            "nutrients": self.nutrients
        }

        

class Meal(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    sumarize = db.Column(db.String(120), unique=False, nullable=False)
    nutrients = db.Column(db.String(80), unique=False, nullable=False)
    ingredients = db.Column(db.String(80), unique=False, nullable=False)
    #favorites = db.relationship("Favorites")
    
    def __repr__(self): 
        return f'<Meal {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "nutrients": self.nutrients,
            "ingredients": self.ingredients
        }

class WeeklyPlan(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    breakfast = db.Column(db.String(120), unique=True, nullable=False)
    lunch = db.Column(db.String(120), unique=True, nullable=False)
    dinner = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<WeeklyPlan {self.id}'

    def serialize(self):
        return { 
            "id": self.id,
            "breakfast": self.breakfast,
            "lunch": self.lunch,
            "dinner": self.dinner
        }

class dailyPlan(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    breakfast = db.Column(db.String(120), unique=True, nullable=False)
    lunch = db.Column(db.String(120), unique=True, nullable=False)
    dinner = db.Column(db.String(120), unique=True, nullable=False)

class Favorites(db.Model):
   
    id = db.Column(db.Integer,unique=True ,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    meals_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    foods_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    user = db.relationship("User")
    meal = db.relationship("Meal")
    food = db.relationship("Food")

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
       
        return {
            "id": self.id,
            "user_id":self.user_id,
            "meals_id":self.meals_id,
            "foods_id":self.foods_id
        }


#                        Dont know if necessary
   
#   id = db.Column(db.Integer, primary_key=True)
#def __repr__(self):
#       return { "id": self.id}
#def serialize(self): return {}