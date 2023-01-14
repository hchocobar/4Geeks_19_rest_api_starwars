"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Endpoint /user
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = User.query.all()
        results = [user.serialize() for user in users]
        response_body = {"message": "ok",
                         "total_records": len(results),
                         "results": results}
        return response_body, 200
        # return jsonify(response_body), 200
    if request.method == 'POST':
        request_body = request.get_json()
        user = User(email = request_body['email'],
                    password = request_body['password'],
                    is_active = request_body['is_active'])
        db.session.add(user)
        db.session.commit()
        return request_body, 200
        # return jsonify(request_body), 200


# Endpoint /user/<int:user_id>
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        results = user.serialize()
        response_body = {"message": "ok",
                         "total_records": 1,
                         "results": results}
        return response_body, 200
    else:
        response_body = {"message": "record not found"}
        return response_body, 200


# Endpoint /people
@app.route('/people', methods=['GET'])
def people():
    if request.method == 'GET':
        characters = Characters.query.all()
        results = [character.serialize() for character in characters]
        response_body = {"message": "ok",
                         "total_records": len(results),
                         "results": results}
        return response_body, 200


# Endpoint /people/<int:people_id>
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    character = Characters.query.filter_by(id=people_id).first()
    if character:
        results = character.serialize()
        response_body = {"message": "ok",
                         "total_records": 1,
                         "results": results}
        return response_body, 200
    else:
        response_body = {"message": "record not found"}
        return response_body, 200


# Endpoint /planets
@app.route('/planets', methods=['GET'])
def planet():
    if request.method == 'GET':
        planets = Planets.query.all()
        results = [planet.serialize() for planet in planets]
        response_body = {"message": "ok",
                         "total_records": len(results),
                         "results": results}
        return response_body, 200


# Endpoint /planets/<int:planet_id>
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.filter_by(id=planet_id).first()
    if planet:
        results = planet.serialize()
        response_body = {"message": "ok",
                         "total_records": 1,
                         "results": results}
        return response_body, 200
    else:
        response_body = {"message": "record not found"}
        return response_body, 200


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
