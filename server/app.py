#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, jsonify, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api, bcrypt
# Add your model imports
from models import User
from schemas import user_schema


# Authentication Resource classes
class Signup(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return make_response({'error': 'All fields are required.'}, 400)

        if User.query.filter_by(email=email).first():
            return make_response({'error': 'Email already registered.'}, 409)

        user = User(name=name, email=email)
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        return make_response(user_schema.dump(user), 201)

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not user.authenticate(password):
            return make_response({'error': 'Invalid email or password.'}, 401)

        session['user_id'] = user.id
        return make_response(user_schema.dump(user), 200)

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return make_response(user_schema.dump(user), 200)
        return make_response({}, 204)

class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return make_response({}, 204)

class AdminOnly(Resource):
    def get(self):
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if user and user.is_admin:
            return make_response({'message': f'Welcome, Admin {user.name}!'}, 200)
        return make_response({'error': 'Admin access required.'}, 403)

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Logout, '/logout')
api.add_resource(AdminOnly, '/admin-only')

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
