from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

users_fav_planets = db.Table('users_fav_planets',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('planets_id', db.Integer, db.ForeignKey('planets.id')))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    users_favorite_planets = db.relationship('Planets', secondary=users_fav_planets)  # Favoritos

    def __repr__(self):
        return '<Users %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "email": self.email,
                "is_active": self.is_active}


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(20))
    orbital_period = db.Column(db.String(20))
    diameter = db.Column(db.String(20))
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(20))
    population = db.Column(db.String(20))

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "rotation_period": self.rotation_period,
                "orbital_period": self.orbital_period,
                "diameter": self.diameter,
                "climate": self.climate,
                "gravity": self.gravity,
                "terrain": self.terrain,
                "surface_water": self.surface_water,
                "population": self.population}


class Characters (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eyes_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(10))
    gender = db.Column(db.String(50))
    homeworld = db.Column(db.String(50))

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "height": self.height,
                "mass": self.mass,
                "hair_color": self.hair_color,
                "skin_color": self.skin_color,
                "eyes_color": self.eyes_color,
                "birht_year": self.birth_year,
                "gender": self.gender,
                "homeworld": self.homeworld}


class UsersFavCharacters(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    characters_id= db.Column(db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<UsersFavCharacters %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "users_id": self.user_id,
                "characters_id" : self.characters_id}
