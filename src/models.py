from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_planet = db.Table('user_planet',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id')))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planet = db.relationship('Planets', secondary=user_planet)  # Favoritos


    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "email": self.email,
                "is_active": self.is_active}


class Characters (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50))
    height = db.Column(db.Integer)
    eyes_color = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "gender": self.gender,
                "height": self.height,
                "eyes_color": self.eyes_color,
                "hair_color": self.hair_color,
                "skin_color": self.skin_color}


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    climate = db.Column(db.String(100))
    orbital_period = db.Column(db.String(100))
    rotation_period = db.Column(db.String(100))
    diameter = db.Column(db.String(100))

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "population": self.population,
                "terrain": self.terrain,
                "climate": self.climate,
                "orbital_period": self.orbital_period,
                "rotation_period": self.rotation_period,
                "diameter": self.diameter}


