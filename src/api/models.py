from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']

    @classmethod
    def create(cls, **kwargs):
        new_user = cls(**kwargs)
        db.session.add(new_user) #INSERT INTO

        try:
            db.session.commit() #SE EJECUTA EL INSERT INTO
            return new_user
        except Exception as Error: 
            raise Exception(Error.args[0], 400)
    
    def serialize(self):
        return {
            "id" : self.id,
            "username" : self.username
        }
        


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.BigInteger, unique=True, nullable=False) #PREGUNTAR A ERNESTO
    diameter = db.Column(db.Integer, unique=True, nullable=False)
    gravity = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, **kwargs): 
        self.name = kwargs['name']
        self.climate = kwargs['climate']
        self.terrain = kwargs['terrain']
        self.population = kwargs['population']
        self.diameter = kwargs['diameter']
        self.gravity = kwargs['gravity']

    @classmethod
    def create(cls, **kwargs):
        new_planet = cls(**kwargs)
        db.session.add(new_planet) #INSERT INTO

        try:
            db.session.commit() #SE EJECUTA EL INSERT INTO
            return new_planet
        except Exception as Error: 
            raise Exception(Error.args[0], 400)        
    
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "climate" : self.climate,
            "terrain" : self.terrain,
            "population" : self.population,
            "diameter" : self.diameter,
            "gravity" : self.gravity
        }
        

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=True, nullable=False)
    eye_color = db.Column(db.String(120), unique=True, nullable=False)
    skin_color = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, **kwargs): 
        self.name = kwargs['name']
        self.birth_year = kwargs['birth_year']
        self.gender = kwargs['gender']
        self.height = kwargs['height']
        self.eye_color = kwargs['eye_color']
        self.skin_color = kwargs['skin_color']

    @classmethod
    def create(cls, **kwargs):
        new_character = cls(**kwargs)
        db.session.add(new_character) #INSERT INTO

        try: 
            db.session.commit() #SE EJECUTA EL INSERT INTO
            return new_character
        except Exception as error: 
            raise Exception(Error.args[0], 400)
    
    def serialize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "height" : self.height,
            "eye_color" : self.eye_color,
            "skin_color" : self.skin_color
        }

class Planet_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id =  db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __init__(self, **kwargs): 
            self.user_id = kwargs['user_id']
            self.planet_id = kwargs['planet_id']
    
    @classmethod
    def create(cls, **kwargs):
        new_planet_favorite = cls(**kwargs)
        db.session.add(new_planet_favorite) #INSERT INTO

        try:
            db.session.commit() #EJECUTA EL INSERT INTO
            return new_character
        except Exception as error: 
            raise Exception(error.args[0], 400)

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "planet_id" : self.planet_id
        }
    
    
    


# class Character_favorite(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, foreignKey('user.id'))
#     character_id =  db.Column(db.Integer, foreignKey('character.id'))
