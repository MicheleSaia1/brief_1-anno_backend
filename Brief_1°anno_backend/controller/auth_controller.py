from flask import Blueprint, request, jsonify, session
from persistence.db_configuration import get_session
from service import user_service

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "missing data"}), 400

    db = get_session()
    try:
        user = user_service.register(db, data)
        return jsonify({"message": "user created", "user": user.to_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "missing data"}), 400

    db = get_session()
    try:
        user = user_service.login(db, data)

       
        session['user_id'] = user.id_user
        session['role'] = user.role

        return jsonify({"message": "logged in", "user": user.to_dict()}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    finally:
        db.close()


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "logged out"}), 200


@auth_bp.route('/me', methods=['GET'])
def me():
   
    if 'user_id' not in session:
        return jsonify({"error": "logged out"}), 401

    return jsonify({
        "user_id": session['user_id'],
        "role": session['role']
    }), 200