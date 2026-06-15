from flask import session, jsonify
from functools import wraps





def login_required(f):
   
    @wraps(f)
    def decorated(*args, **kwargs):

  
        if 'user_id' not in session:
            return jsonify({"error": "you must log in"}), 401

        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    
    @wraps(f)
    def decorated(*args, **kwargs):

        if 'user_id' not in session:
            return jsonify({"error": "you must log in"}), 401

        if session.get('role') != 'admin':
            return jsonify({"error": "only admin can do this"}), 403

        return f(*args, **kwargs)
    return decorated