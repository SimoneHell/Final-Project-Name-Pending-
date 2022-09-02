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

    @classmethod
    def signup(cls, email, password):
        instance = cls(
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




class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    ingredients_nutrients = db.Column(db.Integer, db.ForeignKey('ingredients.nutrients'))
    total_nutrients = db.relationship.("Ingredients")
    favorites = db.relationship("Favorites")

    def __repr__(self):
        return f'<Meals {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "nutrients": self.ingredients_nutrients
        }

class Ingredients (db.model) : 
id = db.Column(db.Integer, primary_key=True)
name = db.column(db.String(120), unique=True, nullable=False)
nutrients = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Ingredients {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "nutrients": self.nutrients
        }

class WeeklyPlan(db.model):
id = db.Column(db.Integer, primary_key=True)
breakfast = db.column(db.String(120), unique=True, nullable=False)
lunch = db.column(db.String(120), unique=True, nullable=False)
dinner = db.column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<WeeklyPlan {self.id}'

    def serialize(self):
        return { 
            "id": self.id,
            "breakfast": self.breakfast,
            "lunch": self.lunch,
            "dinner": self.dinner
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