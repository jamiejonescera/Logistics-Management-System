import bcrypt
from flask import make_response, jsonify
from app import db
from models.users import User, RoleEnum

def create_user(data):
    try:
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role', 'staff') 

        existing_user_by_username = User.query.filter_by(username=username).first()
        if existing_user_by_username:
            return make_response(jsonify({'error': 'Username already exists'}), 400)

        existing_user_by_email = User.query.filter_by(email=email).first()
        if existing_user_by_email:
            return make_response(jsonify({'error': 'Email already exists'}), 400)

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            username=username,
            password_hash=hashed_password.decode('utf-8'),
            email=email,
            role=RoleEnum[role.upper()] if role.upper() in RoleEnum.__members__ else RoleEnum.STAFF
        )

        db.session.add(new_user)
        db.session.commit()

        user_response = {
            'user_id': new_user.user_id,
            'username': new_user.username,
            'email': new_user.email,
            'role': new_user.role.value,
            'created_at': new_user.created_at,
            'updated_at': new_user.updated_at
        }

        return make_response(jsonify({'message': 'User created successfully', 'user': user_response}), 201)

    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'error': str(e)}), 500)

# def login():
   
