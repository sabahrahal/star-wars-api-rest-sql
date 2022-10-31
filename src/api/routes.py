"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planet, Character, Planet_favorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['POST', 'GET'])
def handle_user():
    if request.method == 'GET':
        users = User.query.all()
        users_dictionaries = []

        for user in users: 
            users_dictionaries.append(user.serialize())

        return jsonify(users_dictionaries), 200
    else: 
        new_user_data = request.json
        try:
            new_user = User.create(**new_user_data)
            return jsonify(new_user.serialize()), 201
        except Exception as error: 
            return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/user/<int:position>', methods=['DELETE'])
def delete_user(position):
    user = User.query.filter_by(id = position).delete()
    db.session.commit()
    return f"User with id = {position} has been deleted"

@api.route('/planets', methods=['POST','GET'])
def handle_planet():
    if request.method == 'GET':
            planets = Planet.query.all()
            planets_dictionaries = []

            for planet in planets: 
                planets_dictionaries.append(planet.serialize())
            
            return jsonify(planets_dictionaries),200
    else:
            new_planet_data = request.json
            try:
                new_planet = Planet.create(**new_planet_data) 
                return jsonify(new_planet.serialize()), 201
            except Exception as error: 
                return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/planet/<int:postion>', methods=['DELETE'])
def delete_planet(position): 
    planet = Planet.query.filter_by(id = position).delete()
    db.session.commit()
    return f"Planet with id = {position} has been deleted"

@api.route('/characters', methods=['POST','GET'])
def handle_character():
    if request.method == 'GET':
        characters = Character.query.all()
        characters_dictionaries = []
        
        for character in characters:
            characters_dictionaries.append(character.serialize())
        
        return jsonify(characters_dictionaries), 200
    else: 
        new_character_data = request.json
        try: 
            new_character = Character.create(**new_character_data)
            return jsonify(new_character.serialize()), 201
        except Exception as error: 
                return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/favorites/characters', methods=['POST'])
def handle_characters_favorites():
    new_character_favorite_data = request.json
    try: 
        new_character_favorite = Character_favorite.create(**new_character_favorite_data)
        return jsonify(new_character_favorite.serialize()), 201
    except Exception as error: 
        return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/character/<int:postion>', methods=['DELETE'])
def delete_character(position): 
    character = Character.query.filter_by(id = position).delete()
    db.session.commit()
    return f"Character with id = {position} has been deleted"

@api.route('/favorites/planets/<int:position>', methods=['GET'])
def handle_planets_favorites_by_id():
    planets_favorites_by_id = Planet_favorite.query.filter_by(user_id = position)
    planets_favorites_by_id_dictionaries = []
    for planet in planets_favorites_by_id:
            planets_favorites_by_id_dictionaries.append(planet.serialize())
        
    return jsonify(planets_favorites_by_id_dictionaries), 200


@api.route('/favorites/planets', methods=['POST'])
def handle_planets_favorites():
        new_planet_favorite_data = request.json
        try: 
            new_planet_favorite = Planet_favorite.create(**new_planet_favorite_data)
            return jsonify(new_planet_favorite.serialize()), 201
        except Exception as error: 
                return jsonify(error.args[0], error.args[1] if len(error.args) > 1 else 500)