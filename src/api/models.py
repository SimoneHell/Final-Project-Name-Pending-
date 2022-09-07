from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Relationships --> https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships

class User(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
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



ingredients = db.Table("ingredients",
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True),
    db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True)
)


class Food(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    nutrients = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<Ingredients {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "nutrients": self.nutrients
        }

        

class Meal(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    nutrients = db.Column(db.String(80), unique=False, nullable=False)
    ingredients = db.Column(db.String(80), unique=False, nullable=False)
    #favorites = db.relationship("Favorites")
    
    def __repr__(self): 
        return f'<Meal {self.name}'

    def serialize(self):
        return { 
            "id": self.id,
            "name": self.name,
            "nutrients": self.ingredients
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
    user = db.relationship("User")
    meals = db.relationship("Meal")

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