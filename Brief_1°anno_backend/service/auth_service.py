

import datetime
import bcrypt
import jwt

from model.user import User
from repository import user_repository

SECRET_KEY = "password"  


# ── REGISTER ──────────

def register(session, data):
    

    
    for field in ['name', 'username', 'email', 'password']:
        if field not in data or len(str(data[field]).strip()) == 0:
            raise ValueError(f"Il campo '{field}' è obbligatorio")

    # Controllo lunghezza minima password
    if len(data['password']) < 4:    ### ricorda di cambiare in 8 
        raise ValueError("La password troppo corta ")

    # Controllo email già esistente nel DB
    if user_repository.get_by_email(session, data['email']):
        raise ValueError("Email già registrata")

    if user_repository.get_by_username(session, data['username']):
        raise ValueError("Username già in uso")

    # Hash della password con bcrypt
    password_hash = bcrypt.hashpw(
        data['password'].encode('utf-8'),
        bcrypt.gensalt()             
    ).decode('utf-8')               

    # Creiamo l'oggetto User con la password già hashata
    new_user = User(
        name=data['name'],
        username=data['username'],
        email=data['email'],
        password=password_hash,
        role=data.get('role', 'user')  
    )

    return user_repository.create(session, new_user)


# ── LOGIN ──

def login(session, data):
    

    if "email" not in data or "password" not in data:
        raise ValueError("Email e password obbligatori!")

    
    user = user_repository.get_by_email(session, data['email'])

  
    if user is None:
        raise ValueError("Credenziali non valide!")

    # bcrypt.checkpw confronta la password in chiaro con l'hash salvato nel DB
    # Restituisce True se corrispondono, False altrimenti
    password_correct = bcrypt.checkpw(
        data['password'].encode('utf-8'),
        user.password.encode('utf-8')
    )

    if not password_correct:
        raise ValueError("Credenziali non valide")

    
    payload = {
        'user_id': user.id_user,
        'email': user.email,
        'role': user.role,
        'exp': datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token,user


 